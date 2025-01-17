from app import app
import requests



#==VARIAVEIS============================================================================================================================

#==FUNÇÕES==============================================================================================================================
@app.get('/exporta')
def get_frist_exporta(empresa="520979", codigo="197667", chave="76309a63a02de7fe581f", saida="html", ativo="1"):
    url = "https://ws1.soc.com.br/WebSoc/exportadados"

    querystring = {"parametro":{"empresa":empresa,"codigo":codigo,"chave":chave,"saida":saida,"ativo":ativo}}
    payload = ""
    headers = {"User-Agent": "insomnia/10.3.0"}
    request = requests.get(url, headers=headers, params=querystring, data=payload)

    return request

def get_second_exporta():
    return 'exporta'

def get_third_exporta():
    return 'exporta'
