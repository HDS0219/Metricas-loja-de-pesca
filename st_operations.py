import streamlit as st

from comparacoes import produtosMaisVendidos, produtosMaisRentaveis

def defineSidebar():
    with (st.sidebar):

        st.header("Escolha o que exibir: ")
        selecao = st.sidebar.selectbox('Análises:', ('Individuais', 'Comparativas', 'Ambas'), key=0)
        st.session_state['exibeAnalises'] = selecao

def exibeAnalisesIndividuais(dfMes):

    st.write("Produtos mais rentáveis do mês: ")
    produtosMaisVendidos(dfMes)
    st.text("")
    st.write("Produtos mais vendidos do mês: ")
    produtosMaisRentaveis(dfMes)
    st.write("Dataframe com as informações do mês:")
    st.dataframe(dfMes)





