import streamlit as st

from comparacoes import produtosMaisVendidos, produtosMaisRentaveis

def exibeAnalisesIndividuais(dfMes):

    st.write("Produtos mais rentáveis do mês: ")
    produtosMaisVendidos(dfMes)
    st.text("")
    st.write("Produtos mais vendidos do mês: ")
    produtosMaisRentaveis(dfMes)

    st.dataframe(dfMes)


def defineSidebar():
    with (st.sidebar):

        st.header("Escolha o que exibir: ")
        selecao = st.sidebar.selectbox('Análises:', ('Individuais', 'Comparativas', 'Ambas'), key=0)
        st.session_state['exibeAnalises'] = selecao



