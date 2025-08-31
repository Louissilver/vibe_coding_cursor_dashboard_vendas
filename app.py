import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go

from database import SalesData
from visualizations import SalesVisualizations

# Configuração da página
st.set_page_config(
    page_title="Dashboard de Vendas - Concessionária",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded",
)

# CSS personalizado
st.markdown(
    """
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        color: #1f77b4;
    }
    .metric-label {
        font-size: 1rem;
        color: #666;
    }
</style>
""",
    unsafe_allow_html=True,
)


@st.cache_resource(ttl=300)  # Cache por 5 minutos para recursos de banco
def load_data():
    """Carrega dados do banco com cache"""
    try:
        sales_data = SalesData()
        return sales_data
    except Exception as e:
        st.error(f"Erro ao conectar com o banco de dados: {e}")
        return None


def main():
    # Cabeçalho
    st.markdown(
        '<h1 class="main-header">🚗 Dashboard de Vendas - Concessionária</h1>',
        unsafe_allow_html=True,
    )

    # Carrega dados
    sales_data = load_data()
    if sales_data is None:
        st.error(
            "Não foi possível conectar com o banco de dados. Verifique as configurações."
        )
        return

    viz = SalesVisualizations()

    # Sidebar para filtros
    st.sidebar.title("📊 Filtros")

    # Filtro de período
    st.sidebar.subheader("Período")
    period_option = st.sidebar.selectbox(
        "Selecione o período:",
        [
            "Todos os dados",
            "Últimos 30 dias",
            "Últimos 90 dias",
            "Último ano",
            "Período personalizado",
        ],
    )

    start_date = None
    end_date = None

    if period_option == "Últimos 30 dias":
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
    elif period_option == "Últimos 90 dias":
        end_date = datetime.now()
        start_date = end_date - timedelta(days=90)
    elif period_option == "Último ano":
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365)
    elif period_option == "Período personalizado":
        start_date = st.sidebar.date_input(
            "Data inicial", datetime.now() - timedelta(days=30)
        )
        end_date = st.sidebar.date_input("Data final", datetime.now())
        start_date = datetime.combine(start_date, datetime.min.time())
        end_date = datetime.combine(end_date, datetime.max.time())

    # Carrega dados com filtro de período
    if start_date and end_date:
        recent_sales = sales_data.get_sales_period(start_date, end_date)
        st.sidebar.info(
            f"Período: {start_date.strftime('%d/%m/%Y')} a {end_date.strftime('%d/%m/%Y')}"
        )
    else:
        recent_sales = sales_data.get_recent_sales(1000)  # Últimas 1000 vendas

    # Métricas principais
    st.subheader("📈 Métricas Principais")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        total_sales = sales_data.get_total_sales()
        if not total_sales.empty:
            total_vendas = total_sales["total_vendas"].iloc[0]
            st.metric("Total de Vendas", f"{total_vendas:,}".replace(",", "."))

    with col2:
        if not total_sales.empty:
            valor_total = total_sales["valor_total_vendas"].iloc[0]
            st.metric(
                "Valor Total",
                f"R$ {valor_total:,.2f}".replace(",", "X")
                .replace(".", ",")
                .replace("X", "."),
            )

    with col3:
        if not total_sales.empty:
            valor_medio = total_sales["valor_medio_venda"].iloc[0]
            st.metric(
                "Valor Médio",
                f"R$ {valor_medio:,.2f}".replace(",", "X")
                .replace(".", ",")
                .replace("X", "."),
            )

    with col4:
        if not recent_sales.empty:
            vendas_periodo = len(recent_sales)
            st.metric("Vendas no Período", f"{vendas_periodo:,}".replace(",", "."))

    st.markdown("---")

    # Gráficos principais
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🚗 Vendas por Modelo")
        sales_by_model = sales_data.get_sales_by_model()
        if not sales_by_model.empty:
            fig_model = viz.create_sales_by_model_chart(sales_by_model)
            if fig_model:
                st.plotly_chart(fig_model, use_container_width=True)
        else:
            st.info("Nenhum dado de vendas por modelo disponível.")

    with col2:
        st.subheader("📅 Vendas por Mês")
        sales_by_month = sales_data.get_sales_by_month()
        if not sales_by_month.empty:
            fig_month = viz.create_sales_by_month_chart(sales_by_month)
            if fig_month:
                st.plotly_chart(fig_month, use_container_width=True)
        else:
            st.info("Nenhum dado de vendas por mês disponível.")

    # Gráficos de concessionárias e vendedores
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🏢 Vendas por Concessionária")
        sales_by_dealership = sales_data.get_sales_by_dealership()
        if not sales_by_dealership.empty:
            fig_dealership = viz.create_sales_by_dealership_chart(sales_by_dealership)
            if fig_dealership:
                st.plotly_chart(fig_dealership, use_container_width=True)
        else:
            st.info("Nenhum dado de vendas por concessionária disponível.")

    with col2:
        st.subheader("👥 Vendas por Vendedor")
        sales_by_salesperson = sales_data.get_sales_by_salesperson()
        if not sales_by_salesperson.empty:
            fig_salesperson = viz.create_sales_by_salesperson_chart(
                sales_by_salesperson
            )
            if fig_salesperson:
                st.plotly_chart(fig_salesperson, use_container_width=True)
        else:
            st.info("Nenhum dado de vendas por vendedor disponível.")

    # Gráficos adicionais
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🥧 Distribuição por Modelo")
        if not sales_by_model.empty:
            fig_pie = viz.create_pie_chart_models(sales_by_model)
            if fig_pie:
                st.plotly_chart(fig_pie, use_container_width=True)

    with col2:
        st.subheader("📊 Tendência de Vendas")
        if not recent_sales.empty:
            fig_trend = viz.create_sales_trend_chart(recent_sales)
            if fig_trend:
                st.plotly_chart(fig_trend, use_container_width=True)

    # Tabela de vendas recentes
    st.markdown("---")
    st.subheader("📋 Vendas Recentes")

    if not recent_sales.empty:
        # Formata a coluna de data
        recent_sales_display = recent_sales.copy()
        recent_sales_display["data_venda"] = recent_sales_display[
            "data_venda"
        ].dt.strftime("%d/%m/%Y %H:%M")
        recent_sales_display["valor_pago"] = recent_sales_display["valor_pago"].apply(
            lambda x: f"R$ {x:,.2f}".replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )

        # Renomeia colunas
        recent_sales_display.columns = [
            "Data/Hora",
            "Modelo",
            "Concessionária",
            "Vendedor",
            "Cliente",
            "Valor Pago",
        ]

        st.dataframe(recent_sales_display, use_container_width=True, hide_index=True)
    else:
        st.info("Nenhuma venda recente encontrada.")

    # Informações adicionais
    st.markdown("---")
    st.subheader("ℹ️ Informações do Sistema")

    col1, col2 = st.columns(2)

    with col1:
        st.info(
            """
        **Funcionalidades disponíveis:**
        - 📊 Visualização de métricas principais
        - 🚗 Análise de vendas por modelo
        - 📅 Análise temporal de vendas
        - 🏢 Comparação entre concessionárias
        - 👥 Performance dos vendedores
        - 📋 Lista de vendas recentes
        """
        )

    with col2:
        st.info(
            """
        **Filtros disponíveis:**
        - Período de análise
        - Filtros por data
        - Visualizações interativas
        - Exportação de dados
        """
        )

    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #666;'>"
        "Dashboard de Vendas - Concessionária | Desenvolvido com Streamlit e Plotly"
        "</div>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
