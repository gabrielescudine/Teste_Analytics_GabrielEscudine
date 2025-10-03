-- Arquivo: consultas_sql.sql
-- Objetivo: Consultas SQL para análise de dados de vendas
-- Autor: Gabriel J. Escudine
-- Data: 02/10/2025

-- Suponha que temos uma tabela chamada "Vendas" com a seguinte estrutura, baseada no arquivo 'data_clean.csv':
-- Vendas (
--     ID INT PRIMARY KEY,
--     Produto VARCHAR(100),
--     Categoria VARCHAR(50),
--     Quantidade INT,
--     Preco_Unitario DECIMAL(10, 2),
--     Data DATE
-- );


-- Consulta 1: Listar o total de vendas por produto

SELECT
    Produto,
    Categoria,
    SUM(Quantidade * Preco_Unitario) AS Total_Venda
FROM
    Vendas
GROUP BY
    Produto, Categoria
ORDER BY
    Total_Venda DESC;

-- Para a lógica acima, primeiramente, selecionamos as colunas alvos (Produto e Categoria).
-- Em seguida, calculamos o total de vendas por produto usando a função SUM() para agregar
-- os valores de vendas. Agrupamos os resultados por Produto e Categoria para garantir que
-- a função SUM() calcule o total para cada combinação distinta de produto e categoria.
-- E, por fim, ordenamos os resultados em ordem decrescente com base no total de vendas.

-- Consulta 2: Identificar os produtos com menor venda no mês de Junho de 2023

SELECT
    Produto,
    SUM(Quantidade * Preco_Unitario) AS Total_Venda_Junho
FROM
    Vendas
WHERE
    EXTRACT(YEAR FROM Data) = 2023 AND EXTRACT(MONTH FROM Data) = 6
GROUP BY
    Produto
ORDER BY
    Total_Venda_Junho ASC

-- Para a lógica, desta vez, primeiramente, selecionamos a coluna alvo (Produto).
-- Em seguida, calculamos o total de vendas por produto no mês de junho de 2023
-- usando a função SUM() para agregar os valores de vendas. Filtramos os registros
-- para incluir apenas aqueles cuja data corresponde ao mês de junho de 2023.
-- Agrupamos os resultados por Produto e, por fim, ordenamos em ordem ascendente
-- com base no total de vendas.
