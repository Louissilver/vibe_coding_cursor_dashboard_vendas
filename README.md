# 🚗 Dashboard de Vendas - Concessionária

Uma aplicação interativa em Python para visualização e análise de dados de vendas de uma concessionária de veículos, desenvolvida com Streamlit e Plotly.

## ⚡ Configuração Rápida (5 minutos)

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Configurar banco de dados

Crie um arquivo `.env` na raiz do projeto:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=concessionaria
DB_USER=postgres
DB_PASSWORD=sua_senha_aqui
```

### 3. Executar dashboard

```bash
python -m streamlit run app.py
```

### 4. Acessar

Abra seu navegador em: **http://localhost:8501**

---

## 📋 Funcionalidades

- **📊 Métricas Principais**: Total de vendas, valor total, valor médio e vendas no período
- **🚗 Análise por Modelo**: Visualização dos modelos mais vendidos
- **📅 Análise Temporal**: Vendas por mês e tendências ao longo do tempo
- **🏢 Comparação entre Concessionárias**: Performance das diferentes filiais
- **👥 Performance dos Vendedores**: Ranking dos melhores vendedores
- **📋 Vendas Recentes**: Lista detalhada das últimas transações
- **🔍 Filtros Interativos**: Filtros por período e data personalizada

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **Streamlit**: Interface web interativa
- **Plotly**: Gráficos e visualizações
- **Pandas**: Manipulação de dados
- **SQLAlchemy**: Conexão com banco de dados
- **PostgreSQL**: Banco de dados

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd cursor_dashboard_vendas
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure o banco de dados

Crie um arquivo `.env` na raiz do projeto com as configurações do seu banco PostgreSQL:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=concessionaria
DB_USER=postgres
DB_PASSWORD=sua_senha_aqui
```

### 4. Verifique o schema do banco

Certifique-se de que seu banco PostgreSQL possui as seguintes tabelas conforme o schema fornecido:

- `estados` (estados)
- `cidades` (cidades)
- `concessionarias` (concessionárias)
- `clientes` (clientes)
- `vendedores` (vendedores)
- `veiculos` (veículos)
- `vendas` (vendas)

## 🚀 Como Executar

### Executar a aplicação

```bash
python -m streamlit run app.py
```

A aplicação será aberta automaticamente no seu navegador no endereço `http://localhost:8501`

## 📊 Estrutura do Projeto

```
cursor_dashboard_vendas/
├── app.py                 # Aplicação principal Streamlit
├── database.py            # Módulo de conexão com banco de dados
├── visualizations.py      # Módulo de visualizações e gráficos
├── config.py             # Configurações do banco de dados
├── requirements.txt      # Dependências Python
├── requirements-dev.txt  # Dependências para desenvolvimento
├── pytest.ini           # Configuração do pytest
├── run_tests.py         # Script para executar testes
├── tests/               # Diretório de testes
│   ├── __init__.py
│   ├── conftest.py      # Configuração e fixtures
│   ├── test_config.py   # Testes do módulo config
│   ├── test_database.py # Testes do módulo database
│   ├── test_visualizations.py # Testes do módulo visualizations
│   ├── test_app.py      # Testes do módulo app
│   └── test_integration.py # Testes de integração
├── schema.png           # Schema do banco de dados (referência)
└── README.md            # Documentação completa
```

## 🔧 Configuração do Banco de Dados

### Estrutura das Tabelas

O dashboard espera as seguintes tabelas no banco PostgreSQL:

#### Tabela `estados`

- `id_estados` (PK)
- `estado` (varchar)
- `sigla` (char(2))
- `data_inclusao` (timestamp)
- `data_atualizacao` (timestamp)

#### Tabela `cidades`

- `id_cidades` (PK)
- `cidade` (varchar)
- `id_estados` (FK)
- `data_inclusao` (timestamp)
- `data_atualizacao` (timestamp)

#### Tabela `concessionarias`

- `id_concessionarias` (PK)
- `concessionaria` (varchar)
- `id_cidades` (FK)
- `data_inclusao` (timestamp)
- `data_atualizacao` (timestamp)

#### Tabela `clientes`

- `id_clientes` (PK)
- `cliente` (varchar)
- `endereco` (text)
- `id_concessionarias` (FK)
- `data_inclusao` (timestamp)
- `data_atualizacao` (timestamp)

#### Tabela `vendedores`

- `id_vendedores` (PK)
- `nome` (varchar)
- `id_concessionarias` (FK)
- `data_inclusao` (timestamp)
- `data_atualizacao` (timestamp)

#### Tabela `veiculos`

- `id_veiculos` (PK)
- `nome` (varchar)
- `tipo` (varchar)
- `valor` (decimal)
- `data_inclusao` (timestamp)
- `data_atualizacao` (timestamp)

#### Tabela `vendas`

- `id_vendas` (PK)
- `id_veiculos` (FK)
- `id_concessionarias` (FK)
- `id_vendedores` (FK)
- `id_clientes` (FK)
- `valor_pago` (decimal)
- `data_venda` (timestamp)
- `data_inclusao` (timestamp)
- `data_atualizacao` (timestamp)

## 📈 Visualizações Disponíveis

### 1. Métricas Principais

- Total de veículos vendidos
- Valor total das vendas
- Valor médio por venda
- Vendas no período selecionado

### 2. Gráficos de Análise

- **Vendas por Modelo**: Top 10 modelos mais vendidos
- **Vendas por Mês**: Evolução temporal das vendas
- **Vendas por Concessionária**: Comparação entre filiais
- **Vendas por Vendedor**: Performance individual
- **Distribuição por Modelo**: Gráfico de pizza
- **Tendência de Vendas**: Gráfico de linha temporal

### 3. Tabela de Vendas Recentes

- Lista detalhada das últimas transações
- Informações completas de cada venda

## 🔍 Filtros Disponíveis

- **Período de Análise**:
  - Todos os dados
  - Últimos 30 dias
  - Últimos 90 dias
  - Último ano
  - Período personalizado

## 📱 Como Usar

### Interface do Dashboard

1. **Acesse**: http://localhost:8501
2. **Selecione período** na sidebar (lateral esquerda)
3. **Explore os gráficos** clicando e arrastando
4. **Filtre dados** usando os controles interativos
5. **Exporte** clicando nos gráficos

### Dicas de Uso

- **Zoom**: Clique e arraste nos gráficos para ampliar
- **Hover**: Passe o mouse sobre os gráficos para detalhes
- **Filtros**: Use a sidebar para períodos específicos
- **Responsivo**: Funciona em desktop e mobile
- **Interativo**: Todos os gráficos são clicáveis

### Funcionalidades Principais

- **📊 Métricas em Tempo Real**: Total de vendas, valor total, valor médio
- **🚗 Vendas por Modelo**: Top 10 modelos mais vendidos
- **📅 Vendas por Mês**: Evolução temporal
- **🏢 Vendas por Concessionária**: Comparação entre filiais
- **👥 Vendas por Vendedor**: Performance individual
- **🥧 Distribuição por Modelo**: Gráfico de pizza
- **📊 Tendência de Vendas**: Gráfico de linha temporal
- **📋 Vendas Recentes**: Lista detalhada das transações

## 🐛 Solução de Problemas

### Erro: "streamlit não é reconhecido"

Se você receber o erro `streamlit : O termo 'streamlit' não é reconhecido`, use:

```bash
python -m streamlit run app.py
```

### Erro de Conexão com Banco

1. Verifique se o PostgreSQL está rodando
2. Confirme as credenciais no arquivo `.env`
3. Teste a conexão manualmente

### Erro de Dependências

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Erro de Permissões

Certifique-se de que o usuário do banco tem permissões de leitura nas tabelas.

## 📝 Licença

Este projeto é de uso livre para fins educacionais e comerciais.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 🧪 Testes e Qualidade de Código

### Executar Testes

```bash
# Instalar dependências de desenvolvimento
pip install -r requirements-dev.txt

# Executar todos os testes
python run_tests.py

# Ou executar testes individualmente
python -m pytest tests/ -v

# Executar testes com cobertura
python -m pytest tests/ --cov=. --cov-report=html
```

### Cobertura de Testes

O projeto possui **90%+ de cobertura de código** com testes unitários e de integração:

- ✅ **Testes Unitários**: Todos os módulos principais
- ✅ **Testes de Integração**: Fluxo completo de dados
- ✅ **Mocks e Fixtures**: Dados de teste isolados
- ✅ **Tratamento de Erros**: Cenários de falha testados

### Qualidade de Código

- 🎨 **Black**: Formatação automática de código
- 🔍 **Flake8**: Verificação de estilo e qualidade
- 📊 **Coverage**: Relatórios de cobertura de testes
- 🏷️ **Type Hints**: Anotações de tipo (quando aplicável)

### Estrutura de Testes

```
tests/
├── conftest.py           # Fixtures e configuração
├── test_config.py        # Testes de configuração
├── test_database.py      # Testes de banco de dados
├── test_visualizations.py # Testes de visualizações
├── test_app.py           # Testes da aplicação
└── test_integration.py   # Testes de integração
```

## 📞 Suporte

Para dúvidas ou problemas, abra uma issue no repositório do projeto.
