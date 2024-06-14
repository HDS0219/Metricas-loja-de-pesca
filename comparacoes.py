import pandas as pd
import streamlit as st
from matplotlib.pyplot import figure, ylabel, tight_layout, bar, gca, xticks, xlabel, subplots, barh, text, title
from path_reader import getCaminhoPasta, padrao, getTabelas
from dfs import armazenaDfs

pasta = getCaminhoPasta(padrao)
tabelas = getTabelas(pasta)
listaDf = armazenaDfs(tabelas, pasta)

# Exibe gráficos de df correspondente ao arquivo escolhido na seleção múltipla:

def identificaDf(mes):

    for i in range(len(tabelas)):

        if mes == tabelas[i]:

            print("Análise do mês do arquivo " + tabelas[i])
            dfCorrespondente = listaDf[i]

            return dfCorrespondente

# Análises Individuais:

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
    graf = figure(figsize=(12, 8))
    barh(top_10_itens['Nome Produto'], top_10_itens['Vendas'], color='skyblue')
    xlabel('número de vendas')
    ylabel('Nome Produto')
    title('10 itens mais vendidos no mês')
    gca().invert_yaxis()  # Inverte a ordem dos itens para que o mais vendido fique no topo
    tight_layout()  # Ajusta o layout para se adequar ao tamanho da figura
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
    graf = figure(figsize=(12, 8))
    barh(top_10_itens['Nome Produto'], top_10_itens['Valor'], color='skyblue')
    xlabel('Valor total com vendas')
    ylabel('Nome Produto')
    title('Itens mais rentáveis do mês')
    gca().invert_yaxis()  # Inverte a ordem dos itens para que o mais vendido fique no topo
    tight_layout()  # Ajusta o layout para se adequar ao tamanho da figura
    st.pyplot(graf)


# Análises Comparativas:

def exibeVariacoesDf(df1, df2):
    
    
    # Filtrar valores negativos de 'Valor'
    df1 = df1[df1['Valor'] >= 0]
    df2 = df2[df2['Valor'] >= 0]
    
    # Agrupar por 'Classe' e somar 'Vendas' e 'Valor' para cada mês
    total_vendas_df1 = df1.groupby('Classe')[['Vendas', 'Valor']].sum().reset_index()
    total_vendas_df2 = df2.groupby('Classe')[['Vendas', 'Valor']].sum().reset_index()
    
    # Renomear colunas para diferenciar os meses
    total_vendas_df1.rename(columns={'Vendas': 'Vendas_mes1', 'Valor': 'Valor_mes1'}, inplace=True)
    total_vendas_df2.rename(columns={'Vendas': 'Vendas_mes2', 'Valor': 'Valor_mes2'}, inplace=True)
    
    # Combinar os dados dos dois meses
    total_vendas = pd.merge(total_vendas_df1, total_vendas_df2, on='Classe', how='outer').fillna(0)
    
    # Calcular a porcentagem de aumento em Vendas
    total_vendas['Vendas_Porcentagem'] = ((total_vendas['Vendas_mes2'] - total_vendas['Vendas_mes1']) / total_vendas['Vendas_mes2']) * 100
    
    # Calcular a porcentagem de aumento em Valor
    total_vendas['Valor_Porcentagem'] = ((total_vendas['Valor_mes2'] - total_vendas['Valor_mes1']) / total_vendas['Valor_mes1']) * 100
    
    # Verifique o resultado final
    print("\nComparação de Vendas e Valor por Classe (Janeiro para Fevereiro):")
    st.dataframe(total_vendas[['Classe', 'Vendas_mes1', 'Vendas_mes2', 'Vendas_Porcentagem', 'Valor_mes1', 'Valor_mes2', 'Valor_Porcentagem']])

def exibeVariacaoVenda(df1, df2):
 
    # Filtrar valores negativos de 'Valor'
    df1 = df1[df1['Valor'] >= 0]
    df2 = df2[df2['Valor'] >= 0]
    
    # Agrupar por 'Classe' e somar 'Valor' para cada mês
    total_vendas_df1 = df1.groupby('Classe')['Valor'].sum().reset_index()
    total_vendas_df2 = df2.groupby('Classe')['Valor'].sum().reset_index()
    
    # Renomear colunas para diferenciar os meses
    total_vendas_df1.rename(columns={'Valor': 'Valor_1'}, inplace=True)
    total_vendas_df2.rename(columns={'Valor': 'Valor_2'}, inplace=True)
    
    # Combinar os dados dos dois meses
    total_vendas = pd.merge(total_vendas_df1, total_vendas_df2, on='Classe', how='outer').fillna(0)
    
    # Calcular a porcentagem de aumento
    total_vendas['Aumento_Porcentagem'] = ((total_vendas['Valor_2'] - total_vendas['Valor_1']) / total_vendas['Valor_1']) * 100
    
    # Criar gráfico de barras com as porcentagens de aumento
    graph = figure(figsize=(10, 6))
    bars = bar(total_vendas['Classe'], total_vendas['Aumento_Porcentagem'], color='skyblue')
    
    # Adicionar rótulos de porcentagem acima de cada barra
    for bar in bars:
        yval = bar.get_height()
        text(bar.get_x() + bar.get_width() / 2, yval, f'{yval:.2f}%', ha='center', va='bottom')
    
    xlabel('Classe')
    ylabel('Aumento em Porcentagem')
    title('Aumento em Porcentagem do Valor Total de Vendas por Classe (Janeiro para Fevereiro)')
    xticks(rotation=45)  # Rotaciona os rótulos do eixo x, se necessário
    tight_layout()  # Ajusta o layout para se adequar ao tamanho da figura
    st.pyplot(graph)

def exibeVariacaoValor(df1, df2):

    # Filtrar valores negativos de 'Valor'
    df1 = df1[df1['Valor'] >= 0]
    df2 = df2[df2['Valor'] >= 0]
    
    # Agrupar por 'Classe' e somar 'Valor' para cada mês
    total_vendas_df1 = df1.groupby('Classe')['Valor'].sum().reset_index()
    total_vendas_df2 = df2.groupby('Classe')['Valor'].sum().reset_index()
    
    # Renomear colunas para diferenciar os meses
    total_vendas_df1.rename(columns={'Valor': 'Valor_1'}, inplace=True)
    total_vendas_df2.rename(columns={'Valor': 'Valor_2'}, inplace=True)
    
    # Combinar os dados dos dois meses
    total_vendas = pd.merge(total_vendas_df1, total_vendas_df2, on='Classe', how='outer').fillna(0)
    
    # Calcular a porcentagem do valor total de vendas para cada mês
    total_vendas['Porcentagem_Jan'] = (total_vendas['Valor_1'] / total_vendas['Valor_1'].sum()) * 100
    total_vendas['Porcentagem_Fev'] = (total_vendas['Valor_2'] / total_vendas['Valor_2'].sum()) * 100
    
    # Configurar o gráfico de barras
    fig, ax = subplots(figsize=(12, 8))
    
    # Definir a largura das barras
    bar_width = 0.35
    
    # Definir a posição das barras no eixo x
    r1 = range(len(total_vendas))
    r2 = [x + bar_width for x in r1]
    
    # Criar as barras
    ax.bar(r1, total_vendas['Porcentagem_Jan'], color='skyblue', width=bar_width, edgecolor='grey', label='Jan')
    ax.bar(r2, total_vendas['Porcentagem_Fev'], color='lightgreen', width=bar_width, edgecolor='grey', label='Fev')
    # Adicionar rótulos e título
    ax.set_xlabel('Classe', fontweight='bold')
    ax.set_ylabel('Porcentagem do Valor Total de Vendas', fontweight='bold')
    ax.set_title('Porcentagem do Valor Total de Vendas por Classe', fontweight='bold')
    ax.set_xticks([r + bar_width / 2 for r in range(len(total_vendas))])
    ax.set_xticklabels(total_vendas['Classe'])
    ax.legend()
    
    # Rotacionar os rótulos do eixo x, se necessário
    xticks(rotation=45)
    
    # Ajustar o layout para se adequar ao tamanho da figura
    tight_layout()
    
    # Mostrar o gráfico
    st.pyplot(fig)
