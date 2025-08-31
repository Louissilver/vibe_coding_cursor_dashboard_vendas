import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd


class SalesVisualizations:
    def __init__(self):
        pass

    def create_total_sales_card(self, data):
        """Cria cards com métricas totais"""
        if data.empty:
            return None

        total_vendas = data["total_vendas"].iloc[0]
        valor_total = data["valor_total_vendas"].iloc[0]
        valor_medio = data["valor_medio_venda"].iloc[0]

        # Formatação dos valores
        valor_total_fmt = (
            f"R$ {valor_total:,.2f}".replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )
        valor_medio_fmt = (
            f"R$ {valor_medio:,.2f}".replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )

        return {
            "total_vendas": total_vendas,
            "valor_total": valor_total_fmt,
            "valor_medio": valor_medio_fmt,
        }

    def create_sales_by_model_chart(self, data):
        """Cria gráfico de vendas por modelo"""
        if data.empty:
            return None

        # Limita a 10 modelos para melhor visualização
        top_models = data.head(10)

        fig = px.bar(
            top_models,
            x="modelo",
            y="quantidade_vendida",
            title="Top 10 Modelos Mais Vendidos",
            labels={"modelo": "Modelo", "quantidade_vendida": "Quantidade Vendida"},
            color="valor_total",
            color_continuous_scale="viridis",
        )

        fig.update_layout(xaxis_tickangle=-45, height=500, showlegend=False)

        return fig

    def create_sales_by_month_chart(self, data):
        """Cria gráfico de vendas por mês"""
        if data.empty:
            return None

        fig = px.line(
            data,
            x="nome_mes",
            y="quantidade_vendida",
            title="Vendas por Mês",
            labels={"nome_mes": "Mês", "quantidade_vendida": "Quantidade Vendida"},
            markers=True,
        )

        fig.update_layout(xaxis_tickangle=-45, height=400)

        return fig

    def create_sales_by_dealership_chart(self, data):
        """Cria gráfico de vendas por concessionária"""
        if data.empty:
            return None

        # Limita a 10 concessionárias para melhor visualização
        top_dealerships = data.head(10)

        fig = px.bar(
            top_dealerships,
            x="concessionaria",
            y="valor_total",
            title="Top 10 Concessionárias por Valor de Vendas",
            labels={
                "concessionaria": "Concessionária",
                "valor_total": "Valor Total (R$)",
            },
            color="quantidade_vendida",
            color_continuous_scale="plasma",
            hover_data=["cidade", "estado"],
        )

        fig.update_layout(xaxis_tickangle=-45, height=500, showlegend=False)

        return fig

    def create_sales_by_salesperson_chart(self, data):
        """Cria gráfico de vendas por vendedor"""
        if data.empty:
            return None

        # Limita a 15 vendedores para melhor visualização
        top_salespeople = data.head(15)

        fig = px.bar(
            top_salespeople,
            x="vendedor",
            y="valor_total",
            title="Top 15 Vendedores por Valor de Vendas",
            labels={"vendedor": "Vendedor", "valor_total": "Valor Total (R$)"},
            color="quantidade_vendida",
            color_continuous_scale="inferno",
            hover_data=["concessionaria"],
        )

        fig.update_layout(xaxis_tickangle=-45, height=500, showlegend=False)

        return fig

    def create_sales_trend_chart(self, data):
        """Cria gráfico de tendência de vendas ao longo do tempo"""
        if data.empty:
            return None

        # Agrupa por data e soma as vendas
        daily_sales = (
            data.groupby(data["data_venda"].dt.date)
            .agg({"valor_pago": "sum"})
            .reset_index()
        )

        # Adiciona contagem de vendas
        daily_sales["quantidade"] = (
            data.groupby(data["data_venda"].dt.date).size().values
        )

        # Renomeia as colunas
        daily_sales = daily_sales.rename(
            columns={"data_venda": "data", "valor_pago": "valor_total"}
        )

        fig = make_subplots(
            rows=2,
            cols=1,
            subplot_titles=(
                "Valor Total de Vendas por Dia",
                "Quantidade de Vendas por Dia",
            ),
            vertical_spacing=0.1,
        )

        # Gráfico de valor total
        fig.add_trace(
            go.Scatter(
                x=daily_sales["data"],
                y=daily_sales["valor_total"],
                mode="lines+markers",
                name="Valor Total",
                line=dict(color="blue"),
            ),
            row=1,
            col=1,
        )

        # Gráfico de quantidade
        fig.add_trace(
            go.Scatter(
                x=daily_sales["data"],
                y=daily_sales["quantidade"],
                mode="lines+markers",
                name="Quantidade",
                line=dict(color="red"),
            ),
            row=2,
            col=1,
        )

        fig.update_layout(
            height=600,
            title_text="Tendência de Vendas ao Longo do Tempo",
            showlegend=False,
        )

        return fig

    def create_pie_chart_models(self, data):
        """Cria gráfico de pizza para distribuição de modelos"""
        if data.empty:
            return None

        # Limita a 8 modelos para melhor visualização
        top_models = data.head(8)

        fig = px.pie(
            top_models,
            values="quantidade_vendida",
            names="modelo",
            title="Distribuição de Vendas por Modelo",
        )

        fig.update_layout(height=400)

        return fig

    def create_heatmap_dealership_month(self, data):
        """Cria heatmap de vendas por concessionária e mês"""
        if data.empty:
            return None

        # Verifica se as colunas necessárias existem
        required_columns = ["concessionaria", "nome_mes", "valor_total"]
        if not all(col in data.columns for col in required_columns):
            return None

        # Pivot table para heatmap
        pivot_data = data.pivot_table(
            values="valor_total",
            index="concessionaria",
            columns="nome_mes",
            aggfunc="sum",
            fill_value=0,
        )

        fig = px.imshow(
            pivot_data,
            title="Heatmap de Vendas por Concessionária e Mês",
            labels=dict(x="Mês", y="Concessionária", color="Valor Total (R$)"),
            aspect="auto",
        )

        fig.update_layout(height=500)

        return fig

    def format_currency(self, value):
        """Formata valor para moeda brasileira"""
        return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    def format_number(self, value):
        """Formata número com separadores de milhares"""
        return f"{value:,.0f}".replace(",", ".")
