import pandas as pd

# Inicia um dataframe, utilizando o caminho específico da tabela escolhida:

def iniciaDf(pasta, posicaoLista):

    df = pd.read_excel(pasta + "\\" + posicaoLista, engine="openpyxl")
    return df


# Percorre os índices dentro de "tabelas", então chama a função "iniciaDf" para cada arquivo dentro da lista tabelas,
# retornando uma nova lista com os dataframes de cada tabela.

def armazenaDfs(tabelas, pasta):

    listaDf = []

    for i in range(len(tabelas)):

        dfAtual = iniciaDf(pasta, tabelas[i])
        listaDf.append(dfAtual)

    return listaDf
