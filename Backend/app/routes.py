from flask import render_template, request, jsonify, redirect, url_for
from werkzeug.utils import secure_filename
import os
from app import app
from app.utils import get_frist_exporta, get_second_exporta, get_third_exporta
import requests
# puxo as alterações feitas na instacia do app no arquivo utils.py


#==ROTAS================================================================================================================================
@app.route('/', methods=['GET'])
def init():
    
    empresa="520979"
    codigo="197667"
    chave="76309a63a02de7fe581f"
    saida="html"
    ativo="1"
    url = "https://ws1.soc.com.br/WebSoc/exportadados"

    querystring = {"parametro":'{"empresa":'+empresa+',"codigo":'+codigo+',"chave":'+chave+',"saida":'+saida+',"ativo":'+ativo+'}'}

    response = requests.post(url, params=querystring)
    
    return response.text


# Endpoint que faz a requisição POST para outro serviço
@app.route('/trigger-post', methods=['GET'])
def trigger_post(empresa="520979", codigo="197667", chave="76309a63a02de7fe581f", saida="html", ativo="1"):
    # Dados recebidos da requisição que acionou esse endpoint
    incoming_data = request.get_json()

    # URL do serviço externo para onde você deseja enviar o POST
    external_service_url = 'https://ws1.soc.com.br/WebSoc/exportadados'

    # Dados que serão enviados ao serviço externo
    payload = {
        'key1': incoming_data.get('key1', 'default_value1'),
        'key2': incoming_data.get('key2', 'default_value2')
    }
    querystring = {"parametro":{"empresa":empresa,"codigo":codigo,"chave":chave,"saida":saida,"ativo":ativo}}

    try:
        # Fazendo a requisição POST para o serviço externo
        response = requests.post(external_service_url, params=querystring)

        # Retornando a resposta do serviço externo para o cliente que chamou o endpoint
        return jsonify({
            'status': response.status_code,
            'response': response.json()  # Se a resposta for JSON
        }), response.status_code
    except requests.exceptions.RequestException as e:
        # Tratamento de erros de conexão ou timeout
        return jsonify({'error': str(e)}), 500