import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração inicial do Streamlit
st.set_page_config(page_title="Loja de Pescaria", layout="wide")

# Título do site
st.title("Loja de Pescaria")

# Carregar os dados da planilha Excel do primeiro mês
st.header("Dados do Primeiro Mês")
uploaded_file1 = st.file_uploader("Escolha um arquivo Excel para o Primeiro Mês", type="xlsx", key='file1')
if uploaded_file1 is not None:
    df1 = pd.read_excel(uploaded_file1)

    # Exibir os dados da planilha do primeiro mês
    st.write("Dados da Planilha do Primeiro Mês:")
    st.dataframe(df1)

# Carregar os dados da planilha Excel do segundo mês
st.header("Dados do Segundo Mês")
uploaded_file2 = st.file_uploader("Escolha um arquivo Excel para o Segundo Mês", type="xlsx", key='file2')
if uploaded_file2 is not None:
    df2 = pd.read_excel(uploaded_file2)

    # Exibir os dados da planilha do segundo mês
    st.write("Dados da Planilha do Segundo Mês:")
    st.dataframe(df2)

if uploaded_file1 is not None and uploaded_file2 is not None:
    # Barra lateral para filtros
    st.sidebar.header("Filtrar produtos")
    filtro = st.sidebar.text_input("Filtrar por nome (ex: 'Anzol')", "Anzol")
    num_top_vendas = st.sidebar.number_input("Quantos dos itens mais vendidos você quer ver?", min_value=1,
                                             max_value=100, value=10)

    # Filtrar os dados
    df1_filtrado = df1[df1['Nome Produto'].str.contains(filtro, case=False, na=False)]
    df2_filtrado = df2[df2['Nome Produto'].str.contains(filtro, case=False, na=False)]

    # Exibir os dados filtrados
    st.write(f"Dados filtrados por '{filtro}' do Primeiro Mês:")
    st.dataframe(df1_filtrado)
    st.write(f"Dados filtrados por '{filtro}' do Segundo Mês:")
    st.dataframe(df2_filtrado)

    # Gráfico de vendas por tipo de produto
    if not df1_filtrado.empty and not df2_filtrado.empty:
        df1_agrupado = df1_filtrado.groupby('Nome Produto')['Vendas'].sum().reset_index()
        df1_agrupado['Mês'] = 'Primeiro Mês'
        df2_agrupado = df2_filtrado.groupby('Nome Produto')['Vendas'].sum().reset_index()
        df2_agrupado['Mês'] = 'Segundo Mês'

        df_comparado = pd.concat([df1_agrupado, df2_agrupado])
        df_comparado = df_comparado.groupby('Nome Produto')['Vendas'].sum().reset_index()
        df_comparado = df_comparado.sort_values(by='Vendas', ascending=False).head(num_top_vendas)

        df1_agrupado = df1_agrupado[df1_agrupado['Nome Produto'].isin(df_comparado['Nome Produto'])]
        df2_agrupado = df2_agrupado[df2_agrupado['Nome Produto'].isin(df_comparado['Nome Produto'])]

        df_comparado_final = pd.concat([df1_agrupado, df2_agrupado])

        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(x='Nome Produto', y='Vendas', hue='Mês', data=df_comparado_final, ax=ax)
        ax.set_xlabel(f'Tipo de {filtro}')
        ax.set_ylabel('Total Vendido')
        ax.set_title(f'Comparativo de Vendas por Tipo de {filtro}')
        plt.xticks(rotation=45)

        st.pyplot(fig)

        # Relatório final para o primeiro mês
        quantidade_total1 = df1_filtrado['Vendas'].sum()
        valor_total1 = (df1_filtrado['Vendas'] * df1_filtrado['Valor']).sum()

        st.write(f"**Relatório Final - Primeiro Mês**")
        st.write(f"Quantidade total de itens filtrados ({filtro}): {quantidade_total1}")
        st.write(f"Valor total das vendas de itens filtrados: R${valor_total1:.2f}")

        # Relatório final para o segundo mês
        quantidade_total2 = df2_filtrado['Vendas'].sum()
        valor_total2 = (df2_filtrado['Vendas'] * df2_filtrado['Valor']).sum()

        st.write(f"**Relatório Final - Segundo Mês**")
        st.write(f"Quantidade total de itens filtrados ({filtro}): {quantidade_total2}")
        st.write(f"Valor total das vendas de itens filtrados: R${valor_total2:.2f}")

        # Resumo final comparativo
        if quantidade_total1 > quantidade_total2:
            st.write(f"O Primeiro Mês teve mais vendas de {filtro}, com {quantidade_total1} itens vendidos.")
        else:
            st.write(f"O Segundo Mês teve mais vendas de {filtro}, com {quantidade_total2} itens vendidos.")
