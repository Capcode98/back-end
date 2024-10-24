from app import app


#==VARIAVEIS============================================================================================================================

EXTENCOES_PERMITIDAS = {'csv'}#'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv', 'xlsx', 'json'}
PASTA_DE_UPLOAD = './app/data'
TAMANHO_MAX_PERMITIDO = 16 * 1000 * 1000
#mostrar_grafico = True


app.config['UPLOAD_FOLDER'] = PASTA_DE_UPLOAD
app.config['MAX_CONTENT_LENGTH'] = TAMANHO_MAX_PERMITIDO

#==FUNÇÕES==============================================================================================================================

# retorna o parametro "True" se o arquivo possuir um "."(ponto no nome) e se a extenção estiver dentre as permitidas.
def arquivos_permitidos(NOME_DO_ARQUIVO):
    
    # verifica se o arquivo possui um "."(ponto no nome) e se a extenção está entre as permitidas.
    # a "\" encontrado nesse trecho de código tem a função de fazer a quebra de uma linha de logica e é conhecido como "line-continuation".
    if '.' in NOME_DO_ARQUIVO and \
        NOME_DO_ARQUIVO.rsplit('.', 1)[1].lower() in EXTENCOES_PERMITIDAS:
        return True

