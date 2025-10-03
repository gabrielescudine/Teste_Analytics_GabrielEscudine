# Teste Técnico - Análise de Vendas

Este repositório contém a solução completa para o teste técnico de Análise de Vendas, abrangendo a simulação e limpeza de dados, análise exploratória com visualizações, consultas em SQL e a elaboração de um relatório de insights.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

```bash
├── data/                     # Diretório para armazenar os datasets (não versionado)
├── notebooks/
│   └── analise_vendas.ipynb  # Notebook com a análise exploratória, visualizações
├── sql/
│   └── consultas_sql.sql  # Arquivo SQL com as consultas necessárias
├── src/
│   ├── generate_dataset.py   # Script para gerar o dataset bruto (raw)
│   └── clean_dataset.py      # Script para limpar o dataset e salvá-lo em data/
├── relatorio_insights.md     # Relatório com insights e ações
├── README.md                 # Este arquivo de documentação
├── .gitignore                # Arquivo para ignorar arquivos e diretórios (ex: data/*, venv/)
├── LICENSE                   # Licença do projeto
└── requirements.txt          # Lista de dependências Python
```

## Tecnologias Utilizadas

* **Python 3.10+**
* **Jupyter Notebook:** Para a análise interativa.
* **Pandas:** Para manipulação e análise dos dados.
* **Matplotlib & Seaborn:** Para a criação das visualizações gráficas.
* **SQL:** Para as consultas declarativas de dados.

---

## Instalação e Configuração

Siga os passos abaixo para configurar o ambiente e executar o projeto.

### 1. Clonar o Repositório

```bash
git clone https://github.com/gabrielescudine/Teste_Analytics_GabrielEscudine.git
cd Teste_Analytics_GabrielEscudine
```

### 2. Criar o ambiente virtual e ative-o

```bash
python -m venv venv
venv\Scripts\activate # Para Linux, use source venv/bin/activate
```

### 3. Instale as dependências necessárias

```bash
pip install -r requirements.txt
```

---

## Como Executar o Projeto

Para o funcionamento do projeto, é necessário executar, primeiramente, os scripts responsáveis pela geração dos dados sintéticos.

### 1. Gerando os Dados Sintéticos

Com o comando abaixo, estando na raiz do projeto, é possível realizar a geração dos dados sintéticos.

```bash
python src/generate_dataset.py
```

Por padrão, a seed da geração de números aleatórios é 42, logo, para adquirir os resultados que estão descritos no relatório, **não** altere esse valor. Caso contrário, você poderá ter resultados diferentes dos que foram relatados nesta análise.

### 2. Limpando o Dataset

Em seguida, para realizar uma limpeza nos dados, é necessário executar o seguinte código:

```bash
python src/clean_dataset.py
```

Assim, você terá um dataset com filtros básicos aplicados (remoção de valores NaN, duplicatas, correção de tipo de dados, por exemplo).

No final, você terá o `data_clean.csv`, que é o dataset que foi utilizado para esta análise.

---

## Análise e Resultados

Os entregáveis para cada parte do teste podem ser encontrados nos seguintes locais:

### 1. Análises no `notebooks/analise_vendas.ipynb` e `sql/consultas_sql.sql`

As análises requeridas foram feitas em `notebooks/analise_vendas.ipynb`, onde contém a resposta da Parte 1 do teste. Já a Parte 2 do teste, está em `sql/consultas_sql.sql` com o código SQL e a explicação da lógica utilizada.

### 2. Relatório Final com Insights

Na raiz do projeto, encontra-se o relatório final, que foi produzido após todas as análises feitas. Nele, é possível encontrar os insights que foram extraídos dessa análise e as recomendações ao qual são possíveis de serem tomadas.

---

## Autor

* Gabriel J. Escudine
* LinkedIn: https://www.linkedin.com/in/gabrieljoffilyescudine/
* E-mail: gabrieljescudine.05@gmail.com
