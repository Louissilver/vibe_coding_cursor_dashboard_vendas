"""
Configuração de fixtures para testes
"""

import pytest
import pandas as pd
from datetime import datetime, date
from unittest.mock import Mock, MagicMock
import sys
import os

# Adiciona o diretório raiz ao path para importar módulos
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture
def mock_psycopg2_connection():
    """Mock para conexão psycopg2"""
    mock_conn = Mock()
    mock_cursor = Mock()
    mock_conn.cursor.return_value = mock_cursor
    return mock_conn


@pytest.fixture
def sample_sales_data():
    """Dados de exemplo para vendas"""
    return pd.DataFrame(
        {
            "data_venda": [
                datetime(2024, 1, 15),
                datetime(2024, 1, 16),
                datetime(2024, 1, 17),
                datetime(2024, 2, 1),
                datetime(2024, 2, 2),
            ],
            "modelo": ["Civic", "Corolla", "Civic", "Sentra", "Corolla"],
            "concessionaria": [
                "Concessionária A",
                "Concessionária B",
                "Concessionária A",
                "Concessionária C",
                "Concessionária B",
            ],
            "vendedor": ["João", "Maria", "Pedro", "Ana", "Carlos"],
            "cliente": [
                "Cliente 1",
                "Cliente 2",
                "Cliente 3",
                "Cliente 4",
                "Cliente 5",
            ],
            "valor_pago": [50000.0, 45000.0, 52000.0, 38000.0, 47000.0],
        }
    )


@pytest.fixture
def sample_total_sales_data():
    """Dados de exemplo para total de vendas"""
    return pd.DataFrame(
        {
            "total_vendas": [100],
            "valor_total_vendas": [5000000.0],
            "valor_medio_venda": [50000.0],
        }
    )


@pytest.fixture
def sample_sales_by_model_data():
    """Dados de exemplo para vendas por modelo"""
    return pd.DataFrame(
        {
            "modelo": ["Civic", "Corolla", "Sentra", "Golf", "Jetta"],
            "quantidade_vendida": [25, 20, 15, 12, 8],
            "valor_total": [1250000.0, 1000000.0, 750000.0, 600000.0, 400000.0],
            "valor_medio": [50000.0, 50000.0, 50000.0, 50000.0, 50000.0],
        }
    )


@pytest.fixture
def sample_sales_by_month_data():
    """Dados de exemplo para vendas por mês"""
    return pd.DataFrame(
        {
            "ano": [2024, 2024, 2024, 2024, 2024],
            "mes": [1, 2, 3, 4, 5],
            "nome_mes": ["January", "February", "March", "April", "May"],
            "quantidade_vendida": [30, 25, 20, 15, 10],
            "valor_total": [1500000.0, 1250000.0, 1000000.0, 750000.0, 500000.0],
        }
    )


@pytest.fixture
def sample_sales_by_dealership_data():
    """Dados de exemplo para vendas por concessionária"""
    return pd.DataFrame(
        {
            "concessionaria": [
                "Concessionária A",
                "Concessionária B",
                "Concessionária C",
            ],
            "cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"],
            "estado": ["SP", "RJ", "MG"],
            "quantidade_vendida": [40, 35, 25],
            "valor_total": [2000000.0, 1750000.0, 1250000.0],
            "valor_medio": [50000.0, 50000.0, 50000.0],
        }
    )


@pytest.fixture
def sample_sales_by_dealership_month_data():
    """Dados de exemplo para vendas por concessionária e mês (para heatmap)"""
    return pd.DataFrame(
        {
            "concessionaria": [
                "Concessionária A",
                "Concessionária A",
                "Concessionária B",
                "Concessionária B",
                "Concessionária C",
            ],
            "nome_mes": ["Janeiro", "Fevereiro", "Janeiro", "Fevereiro", "Janeiro"],
            "quantidade_vendida": [20, 15, 18, 12, 10],
            "valor_total": [1000000.0, 750000.0, 900000.0, 600000.0, 500000.0],
        }
    )


@pytest.fixture
def sample_sales_by_salesperson_data():
    """Dados de exemplo para vendas por vendedor"""
    return pd.DataFrame(
        {
            "vendedor": ["João", "Maria", "Pedro", "Ana", "Carlos"],
            "concessionaria": [
                "Concessionária A",
                "Concessionária B",
                "Concessionária A",
                "Concessionária C",
                "Concessionária B",
            ],
            "quantidade_vendida": [15, 12, 10, 8, 6],
            "valor_total": [750000.0, 600000.0, 500000.0, 400000.0, 300000.0],
            "valor_medio": [50000.0, 50000.0, 50000.0, 50000.0, 50000.0],
        }
    )


@pytest.fixture
def mock_db_config():
    """Configuração mock do banco de dados"""
    return {
        "host": "localhost",
        "port": "5432",
        "database": "test_db",
        "user": "test_user",
        "password": "test_password",
    }


@pytest.fixture
def mock_database_url():
    """URL mock do banco de dados"""
    return "postgresql://test_user:test_password@localhost:5432/test_db"


@pytest.fixture
def sample_recent_sales_data():
    """Dados de exemplo para vendas recentes"""
    return pd.DataFrame(
        {
            "data_venda": [
                datetime(2024, 12, 31, 14, 30),
                datetime(2024, 12, 31, 15, 45),
                datetime(2024, 12, 31, 16, 20),
                datetime(2024, 12, 31, 17, 10),
                datetime(2024, 12, 31, 18, 30),
            ],
            "modelo": ["Civic", "Corolla", "Sentra", "Golf", "Jetta"],
            "concessionaria": [
                "Concessionária A",
                "Concessionária B",
                "Concessionária A",
                "Concessionária C",
                "Concessionária B",
            ],
            "vendedor": ["João", "Maria", "Pedro", "Ana", "Carlos"],
            "cliente": [
                "Cliente 1",
                "Cliente 2",
                "Cliente 3",
                "Cliente 4",
                "Cliente 5",
            ],
            "valor_pago": [50000.0, 45000.0, 52000.0, 38000.0, 47000.0],
        }
    )
