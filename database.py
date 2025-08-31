import pandas as pd
import psycopg2
from sqlalchemy import create_engine, text
from config import DATABASE_URL, DB_CONFIG


class DatabaseConnection:
    def __init__(self):
        self.engine = None
        self.connection = None

    def connect(self):
        """Estabelece conexão com o banco de dados"""
        try:
            # Usa psycopg2 diretamente para conexão remota
            self.connection = psycopg2.connect(
                host=DB_CONFIG["host"],
                port=DB_CONFIG["port"],
                database=DB_CONFIG["database"],
                user=DB_CONFIG["user"],
                password=DB_CONFIG["password"],
            )
            return True
        except Exception as e:
            print(f"Erro ao conectar com o banco: {e}")
            return False

    def is_connected(self):
        """Verifica se a conexão está ativa"""
        return self.connection is not None

    def disconnect(self):
        """Fecha a conexão com o banco de dados"""
        if self.connection:
            self.connection.close()
        if self.engine:
            self.engine.dispose()

    def execute_query(self, query, params=None):
        """Executa uma consulta SQL e retorna um DataFrame"""
        try:
            if not self.is_connected():
                print("Erro: Não há conexão ativa com o banco de dados")
                return pd.DataFrame()

            if params:
                df = pd.read_sql_query(query, self.connection, params=params)
            else:
                df = pd.read_sql_query(query, self.connection)
            return df
        except Exception as e:
            print(f"Erro ao executar consulta: {e}")
            return pd.DataFrame()


class SalesData:
    def __init__(self):
        self.db = DatabaseConnection()
        self.connected = self.db.connect()

    def get_total_sales(self):
        """Retorna o total de vendas"""
        if not self.connected:
            print("Erro: Não foi possível conectar com o banco de dados")
            return pd.DataFrame()

        query = """
        SELECT 
            COUNT(*) as total_vendas,
            SUM(valor_pago) as valor_total_vendas,
            AVG(valor_pago) as valor_medio_venda
        FROM vendas
        """
        return self.db.execute_query(query)

    def get_sales_by_model(self):
        """Retorna vendas por modelo de veículo"""
        if not self.connected:
            return pd.DataFrame()

        query = """
        SELECT 
            v.nome as modelo,
            COUNT(*) as quantidade_vendida,
            SUM(ven.valor_pago) as valor_total,
            AVG(ven.valor_pago) as valor_medio
        FROM vendas ven
        JOIN veiculos v ON ven.id_veiculos = v.id_veiculos
        GROUP BY v.id_veiculos, v.nome
        ORDER BY quantidade_vendida DESC
        """
        return self.db.execute_query(query)

    def get_sales_by_month(self, year=None):
        """Retorna vendas por mês"""
        if not self.connected:
            return pd.DataFrame()

        if year:
            query = """
            SELECT 
                EXTRACT(MONTH FROM data_venda) as mes,
                TO_CHAR(data_venda, 'Month') as nome_mes,
                COUNT(*) as quantidade_vendida,
                SUM(valor_pago) as valor_total
            FROM vendas
            WHERE EXTRACT(YEAR FROM data_venda) = %s
            GROUP BY EXTRACT(MONTH FROM data_venda), TO_CHAR(data_venda, 'Month')
            ORDER BY mes
            """
            return self.db.execute_query(query, (year,))
        else:
            query = """
            SELECT 
                EXTRACT(YEAR FROM data_venda) as ano,
                EXTRACT(MONTH FROM data_venda) as mes,
                TO_CHAR(data_venda, 'Month') as nome_mes,
                COUNT(*) as quantidade_vendida,
                SUM(valor_pago) as valor_total
            FROM vendas
            GROUP BY EXTRACT(YEAR FROM data_venda), EXTRACT(MONTH FROM data_venda), TO_CHAR(data_venda, 'Month')
            ORDER BY ano DESC, mes
            """
            return self.db.execute_query(query)

    def get_sales_by_dealership(self):
        """Retorna vendas por concessionária"""
        if not self.connected:
            return pd.DataFrame()

        query = """
        SELECT 
            c.concessionaria,
            ci.cidade,
            es.estado,
            COUNT(*) as quantidade_vendida,
            SUM(ven.valor_pago) as valor_total,
            AVG(ven.valor_pago) as valor_medio
        FROM vendas ven
        JOIN concessionarias c ON ven.id_concessionarias = c.id_concessionarias
        JOIN cidades ci ON c.id_cidades = ci.id_cidades
        JOIN estados es ON ci.id_estados = es.id_estados
        GROUP BY c.id_concessionarias, c.concessionaria, ci.cidade, es.estado
        ORDER BY valor_total DESC
        """
        return self.db.execute_query(query)

    def get_sales_by_salesperson(self):
        """Retorna vendas por vendedor"""
        if not self.connected:
            return pd.DataFrame()

        query = """
        SELECT 
            v.nome as vendedor,
            c.concessionaria,
            COUNT(*) as quantidade_vendida,
            SUM(ven.valor_pago) as valor_total,
            AVG(ven.valor_pago) as valor_medio
        FROM vendas ven
        JOIN vendedores v ON ven.id_vendedores = v.id_vendedores
        JOIN concessionarias c ON v.id_concessionarias = c.id_concessionarias
        GROUP BY v.id_vendedores, v.nome, c.concessionaria
        ORDER BY valor_total DESC
        """
        return self.db.execute_query(query)

    def get_recent_sales(self, limit=10):
        """Retorna as vendas mais recentes"""
        if not self.connected:
            return pd.DataFrame()

        query = """
        SELECT 
            ven.data_venda,
            v.nome as modelo,
            c.concessionaria,
            vend.nome as vendedor,
            cli.cliente,
            ven.valor_pago
        FROM vendas ven
        JOIN veiculos v ON ven.id_veiculos = v.id_veiculos
        JOIN concessionarias c ON ven.id_concessionarias = c.id_concessionarias
        JOIN vendedores vend ON ven.id_vendedores = vend.id_vendedores
        JOIN clientes cli ON ven.id_clientes = cli.id_clientes
        ORDER BY ven.data_venda DESC
        LIMIT %s
        """
        return self.db.execute_query(query, (limit,))

    def get_sales_period(self, start_date, end_date):
        """Retorna vendas em um período específico"""
        if not self.connected:
            return pd.DataFrame()

        query = """
        SELECT 
            ven.data_venda,
            v.nome as modelo,
            c.concessionaria,
            vend.nome as vendedor,
            cli.cliente,
            ven.valor_pago
        FROM vendas ven
        JOIN veiculos v ON ven.id_veiculos = v.id_veiculos
        JOIN concessionarias c ON ven.id_concessionarias = c.id_concessionarias
        JOIN vendedores vend ON ven.id_vendedores = vend.id_vendedores
        JOIN clientes cli ON ven.id_clientes = cli.id_clientes
        WHERE ven.data_venda BETWEEN %s AND %s
        ORDER BY ven.data_venda DESC
        """
        return self.db.execute_query(query, (start_date, end_date))

    def close_connection(self):
        """Fecha a conexão com o banco"""
        self.db.disconnect()
