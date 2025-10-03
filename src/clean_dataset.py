import pandas as pd

def clean_dataset(input_path="./data/data_raw.csv", output_path="./data/data_clean.csv"):
    """
    Função para limpar o dataset removendo linhas com valores nulos, em caso existam.
    - Trata valores nulos;
    - Remove duplicatas;
    - Converte tipos de dados se necessário;
    - Salva em CSV em, por padrão, ../data/data_clean.csv.
    
    Parameters:
        input_path (str): Caminho para o arquivo de entrada. Defaults to "../data/data_raw.csv".
        output_path (str): Caminho para o arquivo de saída. Defaults to "../data/data_clean.csv".
    """
    
    # Carrega o arquivo CSV raw
    df = pd.read_csv(input_path)
    
    # Remove linhas com valores nulos
    df = df.dropna()
    
    # Remove duplicatas
    df = df.drop_duplicates()  
    
    # Ajusta a coluna "Data" para o tipo datetime
    if df['Data'].dtype != 'datetime64[ns]':
        df['Data'] = pd.to_datetime(df['Data'], errors='coerce')
    
    # Ajusta a coluna "Quantidade" para o tipo int
    df['Quantidade'] = df['Quantidade'].astype(int)

    # Ajusta a coluna "Preco_Unitario" para o tipo float
    df['Preco_Unitario'] = df['Preco_Unitario'].astype(float)

    # Salva o dataset limpo em CSV
    df.to_csv(output_path, index=False, encoding='utf-8')
    
    print(f"Dataset limpo salvo em '{output_path}'")
    return df

if __name__ == "__main__":
    clean_dataset(input_path="./data/data_raw.csv", output_path="./data/data_clean.csv")