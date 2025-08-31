# Dashboard de Vendas – Concessionária NovaDrive Motors 🚗📊

## 📌 Motivo da Criação

Este projeto foi desenvolvido como parte de um estudo prático de **Vibe Coding com IA**, utilizando a ferramenta **Cursor** para acelerar o desenvolvimento.  
A ideia surgiu da necessidade de criar uma aplicação interativa que permitisse à **Concessionária NovaDrive Motors** acompanhar em tempo real suas métricas de vendas e gerar insights estratégicos a partir de um banco de dados **PostgreSQL em produção**.

O diferencial é que todo o desenvolvimento foi feito **em poucas horas**, guiado por **prompts bem estruturados** dentro do Cursor, que geraram não apenas o código principal, mas também os testes unitários para garantir qualidade.

---

## 🎯 Objetivo Principal

Criar uma aplicação interativa em **Python** que apresente **visualizações úteis de dados de vendas**, conectando-se a um banco de dados PostgreSQL já existente e populado.

---

## 🏢 Contexto da Aplicação

O sistema é um **Dashboard de Vendas** para a **CONCESSIONÁRIA NOVADRIVE MOTORS**, oferecendo insights estratégicos como:

- Total de veículos vendidos
- Vendas por modelo
- Vendas por mês/período
- Comparação entre filiais

---

## 🗄️ Conectividade e Banco de Dados

- **Banco:** PostgreSQL
- **Status:** Já existe e está populado (não criar banco ou dados de exemplo)
- **Schema:** Disponível em documentação interna e imagem anexa
- **Conexão:** Centralizada em arquivo de configuração próprio

---

## 📊 Funcionalidades e Visualizações

- ✅ Total de veículos vendidos
- ✅ Vendas por modelo
- ✅ Vendas por período (mensal, trimestral, etc.)
- ✅ Comparativo entre filiais
- ✅ Filtros interativos para análise dinâmica

---

## ⚙️ Características Técnicas

- Linguagem: **Python**
- Banco: **PostgreSQL**
- Interatividade: Gráficos dinâmicos e filtráveis
- Estrutura modular para facilitar manutenção e escalabilidade

---

## 🌐 Origem dos Dados

Os dados vêm de um **Banco de Dados “vivo” de vendas na nuvem**

---

## 💡 Prompt Utilizado (Cursor)

### Desenvolvimento

```bash
Quero que você desenvolva uma aplicação interativa em Python que funcione como
um dashboard de vendas para uma concessionária de veículos.
- A aplicação deve se conectar a um banco de dados PostgreSQL
- O banco de dados já existe e já esta populado, você não deve criar o banco ou
criar dados de exemplo
- O schema do banco pode ser visualizado na imagem em anexo
- Crie visualizações úteis para o contexto de vendas, como:
  - Total de veículos vendidos
  - Vendas por modelo
  - Vendas por mês ou período
  - Comparação entre filiais, se houver
- Crie um arquivo de configuração para armazenar dados de conexão com postgres
```

### Testes Unitários

```bash
Você como arquiteto de software e também desenvolvedor senior backend especialista
em python precisa agora desenvolver os testes unitários para ter um bom Code Coverage
e atingir notas satisfatórias no Sonar Qube.
Por favor, gere os arquivos de testes bem como os testes unitários propriamente ditos.
Utilize a stack que melhor lhe aprouver, mas garanta a qualidade do código
```

---

## ✅ Como Rodar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/Louissilver/vibe_coding_cursor_dashboard_vendas.git
   ```
2. Crie e configure o arquivo de conexão (`config.json` ou `.env`) com suas credenciais PostgreSQL.
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Rode a aplicação:
   ```bash
   python app.py
   ```

---

## 🧪 Testes

Para executar os testes unitários:

```bash
pytest
```

Os testes foram gerados também via **prompts no Cursor**, garantindo **bom Code Coverage** e integração com **SonarQube**.
