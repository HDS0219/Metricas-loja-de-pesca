import streamlit as st
import matplotlib.pyplot as plt
from path_reader import getCaminhoPasta, padrao, getTabelas
from dfs import armazenaDfs

pasta = getCaminhoPasta(padrao)
tabelas = getTabelas(pasta)
listaDf = armazenaDfs(tabelas, pasta)

# Exibe gráficos de df correspondente ao arquivo escolhido na seleção múltipla:

def produtosMaisVendidos(df):

    # Agrupando por 'Nome Produto' e somando as 'Vendas'
    total_vendas_por_produto = df.groupby('Nome Produto')['Vendas'].sum().reset_index()

    # Verifique os registros do DataFrame agrupado
    print("\nDataFrame agrupado por 'Nome Produto':")
    print(total_vendas_por_produto.head())

    # Ordenando por 'Vendas' em ordem decrescente e selecionando os 10 itens mais rentáveis
    top_10_itens = total_vendas_por_produto.sort_values(by='Vendas', ascending=False).head(10)

    # Verifique os registros dos 10 itens mais vendidos
    print("\nItens mais vendidos:")
    print(top_10_itens)

    # Criando o gráfico de barras horizontal para os 10 itens mais rentáveis
    graf = plt.figure(figsize=(12, 8))
    plt.barh(top_10_itens['Nome Produto'], top_10_itens['Vendas'], color='skyblue')
    plt.xlabel('número de vendas')
    plt.ylabel('Nome Produto')
    plt.title('10 itens mais vendidos no mês')
    plt.gca().invert_yaxis()  # Inverte a ordem dos itens para que o mais vendido fique no topo
    plt.tight_layout()  # Ajusta o layout para se adequar ao tamanho da figura
    st.pyplot(graf)

def produtosMaisRentaveis(df):

    # Agrupando por 'Nome Produto' e somando as 'Vendas'
    total_vendas_por_produto = df.groupby('Nome Produto')['Valor'].sum().reset_index()

    # Verifique os registros do DataFrame agrupado
    print("\nDataFrame agrupado por 'Nome Produto':")
    print(total_vendas_por_produto.head())

    # Ordenando por 'Vendas' em ordem decrescente e selecionando os 10 itens mais rentáveis
    top_10_itens = total_vendas_por_produto.sort_values(by='Valor', ascending=False).head(10)

    # Verifique os registros dos 10 itens mais vendidos
    print("\nItens mais rentáveis:")
    print(top_10_itens)

    # Criando o gráfico de barras horizontal para os 10 itens mais rentáveis
    graf = plt.figure(figsize=(12, 8))
    plt.barh(top_10_itens['Nome Produto'], top_10_itens['Valor'], color='skyblue')
    plt.xlabel('Valor total com vendas')
    plt.ylabel('Nome Produto')
    plt.title('Itens mais rentáveis do mês')
    plt.gca().invert_yaxis()  # Inverte a ordem dos itens para que o mais vendido fique no topo
    plt.tight_layout()  # Ajusta o layout para se adequar ao tamanho da figura
    st.pyplot(graf)




def identificaDf(mes):

    for i in range(len(tabelas)):

        if mes == tabelas[i]:

            print("Análise do mês do arquivo " + tabelas[i])
            dfCorrespondente = listaDf[i]

            return dfCorrespondente


# def comparaMediaLucro(df)  # retorna medialucro
# def comparaMediaVendas(df) # retorna mediavenda

# def comparaVendasTabelas(df1, df2)
#comparaMediaVendas(df1)
#comparaMediaVendas(df2)

