import pandas as pd
import numpy as np
import random

def generate_dataset(num_registros=100, output_path="./data/data_raw.csv", seed=42):
    """
    Função para gerar um dataset fictício de vendas.

    Parameters:
        num_registros (int): Número de registros a serem gerados. Defaults to 100.
        seed (int): Semente para geração de números aleatórios. Defaults to 42.
        output_path (str): Caminho para o arquivo de saída. Defaults to "../data/data_raw.csv".
    """
    
    # Define a semente para reprodutibilidade
    random.seed(seed)
    np.random.seed(seed)
    
    # Produtos e Categorias
    produtos = {
        "Notebook": "Eletrônicos",
        "Smartphone": "Eletrônicos",
        "Fone de Ouvido": "Eletrônicos",
        "Camiseta": "Vestuário",
        "Calça Jeans": "Vestuário",
        "Tênis": "Vestuário",
        "Geladeira": "Eletrodomésticos",
        "Fogão": "Eletrodomésticos",
        "Microondas": "Eletrodomésticos",
        "Livro": "Livraria",
        "Caneta": "Papelaria",
    }

    # Gera datas aleatórias em 2023, no período selecionado
    datas = pd.date_range(start="2023-01-01", end="2023-12-31")
    datas_aleatorias = np.random.choice(datas, size=num_registros)

    # Gera IDs únicos
    ids = range(1, num_registros + 1)

    # Gera produtos aleatórios
    produtos_aleatorios = random.choices(list(produtos.keys()), k=num_registros)

    # Gera as categorias com base nos produtos
    categorias = [produtos[p] for p in produtos_aleatorios]

    # Gera quantidades aleatórias entre 1 e 20
    quantidades = np.random.randint(1, 21, size=num_registros)

    # Gera os preços com base nos produtos
    precos = []
    for p in produtos_aleatorios:
        if p == "Notebook":
            precos.append(round(np.random.uniform(2500, 5000), 2))
        elif p == "Smartphone":
            precos.append(round(np.random.uniform(1000, 4000), 2))
        elif p == "Fone de Ouvido":
            precos.append(round(np.random.uniform(50, 500), 2))
        elif p == "Camiseta":
            precos.append(round(np.random.uniform(30, 150), 2))
        elif p == "Calça Jeans":
            precos.append(round(np.random.uniform(80, 300), 2))
        elif p == "Tênis":
            precos.append(round(np.random.uniform(150, 800), 2))
        elif p == "Geladeira":
            precos.append(round(np.random.uniform(2000, 6000), 2))
        elif p == "Fogão":
            precos.append(round(np.random.uniform(1000, 3000), 2))
        elif p == "Microondas":
            precos.append(round(np.random.uniform(400, 1200), 2))
        elif p == "Livro":
            precos.append(round(np.random.uniform(20, 150), 2))
        elif p == "Caneta":
            precos.append(round(np.random.uniform(2, 20), 2))

    # Cria o DataFrame com os dados já gerados
    df = pd.DataFrame({
        "ID": ids,
        "Data": datas_aleatorias,
        "Produto": produtos_aleatorios,
        "Categoria": categorias,
        "Quantidade": quantidades,
        "Preco_Unitario": precos
    })

    # Salva o DataFrame em um arquivo CSV
    df.to_csv(output_path, index=False, encoding="utf-8")
    print(f"Dataset gerado com sucesso em '{output_path}'")
    return df

# Executa a função para gerar o dataset
if __name__ == "__main__":
    generate_dataset(num_registros=500, output_path="./data/data_raw.csv")