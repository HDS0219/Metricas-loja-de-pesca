import os
import glob

""" 
Preciso gerar um dataframe, então preciso selecionar a coluna de Vendas, realizando uma soma de tudo. Com isso,
essa soma será dividida por 30 (mês comercial), então será exibida a média de vendas diária desse mês para o outro.

O mesmo deve ser feito para quantidade de produtos de um mês para outro.
"""

# Caminho da pasta com as tabelas:

padrao = r"C:\Users\*\Documents\tabelas"


# Busca e retorna o caminho com o padrão fornecido.

def getCaminhoPasta(caminho, caminho_padrao="caminho_padrao"):
    print(f"Procurando por caminhos que correspondem ao padrão: {caminho}")
    # Procura caminhos que satisfaçam o padrão do argumento dado, e os armazena em uma lista:
    caminhosEncontrados = glob.glob(caminho)

    # Verifica se a lista tem algum caminho encontrado:
    if len(caminhosEncontrados) == 1:
        print("Um caminho correspondente foi encontrado.")
        caminhoTabelas = caminhosEncontrados[0]
        return caminhoTabelas
    elif len(caminhosEncontrados) == 0:
        print("Nenhum caminho correspondente encontrado. Usando caminho padrão.")
        return caminho_padrao
    else:
        print(f"caminhosEncontrados: {caminhosEncontrados}")
        raise ValueError("O caminho não foi encontrado ou existem mais de um caminho correspondente ao padrão. Crie uma e apenas uma pasta 'tabela' na pasta 'Documents.'")

# Utiliza o retorno de getCaminho para listar e retornar os itens de seu diretório.

def getTabelas(pasta):
    listaArquivos = os.listdir(pasta)
    return listaArquivos
