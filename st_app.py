import streamlit as st
from st_operations import defineSidebar, exibeAnalisesIndividuais
from comparacoes import identificaDf, produtosMaisVendidos, produtosMaisRentaveis
from dfs import armazenaDfs
from path_reader import getCaminhoPasta, padrao, getTabelas

# Encontra a pasta com as tabelas:
pasta = getCaminhoPasta(padrao)


# Lista e retorna os itens da pasta:
tabelas = getTabelas(pasta)


# Configuração inicial do Streamlit
st.set_page_config(page_title="Loja de Pescaria", layout="wide")


# Título do site
st.title("Loja de Pescaria Shopping Avenida")


# Inicia dataframes para todas as tabelas encontradas:
listaDf = armazenaDfs(tabelas, pasta)


# Inicia sidebar:
defineSidebar()


# Selectbox com primeiro mês:
primeiroMes = st.selectbox("Primeiro mês: ", tabelas)
dfPrimeiroMes = identificaDf(primeiroMes)


# Selectbox com segundo mês:
segundoMes = st.selectbox("Segundo mês: ", tabelas)
dfSegundoMes = identificaDf(segundoMes)


# Busca opção de exibição selecionada na sidebar:
selecaoEscolhida = st.session_state.get('exibeaddAnalises', 'Individuais')

if selecaoEscolhida == 'Individuais':

    st.header("Análises do primeiro mês: ")
    exibeAnalisesIndividuais(dfPrimeiroMes)

    st.header("Análises do segundo mês: ")
    exibeAnalisesIndividuais(dfSegundoMes)

elif selecaoEscolhida == 'Comparativas':

    st.header("Análises comparativas dos meses escolhidos: ")
    # exibeAnalisesComparativas(df1,df2)

elif selecaoEscolhida == 'Ambas':

    st.header("Análises do primeiro mês: ")
    exibeAnalisesIndividuais(dfPrimeiroMes)

    st.header("Análises do segundo mês: ")
    exibeAnalisesIndividuais(dfSegundoMes)

    st.header("Análises comparativas dos meses escolhidos: ")
    # exibeAnalisesComparativas(df1,df2)