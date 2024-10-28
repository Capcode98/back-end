from flask import render_template, request, redirect, url_for, Response
from werkzeug.utils import secure_filename
import os
# puxo as alterações feitas na instacia do app no arquivo utils.py
from app.utils import app
from auth import jwt


#==ROTAS================================================================================================================================

@app.route('/Login')
@app.route('/Login.html')
def Login():
    return render_template('Login.html')

@app.route('/Tela_analise')
@app.route('/Tela_analise.html')
def Tela_analise():
    nome_do_arquivo = request.args.get('nome')

    if not nome_do_arquivo:
        return "Nenhum arquivo foi selecionado.", 400

    # Renderiza a página Analise.html e passa o nome do arquivo CSV
    return render_template('Tela_analise.html', nome=nome_do_arquivo)


@app.route('/Cadastra')
@app.route('/Cadastra.html')
def Cadastra():
    return render_template('Cadastra.html')

@app.route('/Coleta', methods=['GET', 'POST'])
@app.route('/Coleta.html', methods=['GET', 'POST'])
def Coleta():
    if request.method == 'POST':
        from app.utils import arquivos_permitidos
        arquivo = request.files.get('Arquivo')
        
        if not arquivo or arquivo.filename == '':
            return "Nenhum arquivo foi selecionado.", 400

        # Verifica se o arquivo é permitido
        if not arquivos_permitidos(arquivo.filename):
            return "Tipo de arquivo não permitido.", 400

        # Corrige o nome do arquivo e salva no diretório configurado
        nome_corrigido_do_arquivo = secure_filename(arquivo.filename)
        caminho_arquivo = os.path.join(app.config['UPLOAD_FOLDER'], nome_corrigido_do_arquivo)
        arquivo.save(caminho_arquivo)

        # Redireciona para a página que vai mostrar o gráfico
        return redirect(url_for('Tela_analise', nome=nome_corrigido_do_arquivo))

    return render_template('Coleta.html')


@app.route('/IndexCadastrado')
@app.route('/IndexCadastrado.html')
@app.route('/indexCadastrado')
@app.route('/indexCadastrado.html')
def IndexCadastro():
    return render_template('IndexCadastrado.html')

@app.route('/')
@app.route('/Init')
@app.route('/Init.html')
def Init():
    return render_template('Index.html')

@app.route('/plot.png')
def plot_png():
    # Pega o nome do arquivo CSV via parâmetro da URL
    nome_do_arquivo = request.args.get('nome')
    
    # Verifica se o nome do arquivo foi passado
    if not nome_do_arquivo:
        return "Nome do arquivo CSV não foi fornecido.", 400

    # Cria o caminho completo para o arquivo CSV
    caminho_arquivo_csv = os.path.join(app.config['UPLOAD_FOLDER'], nome_do_arquivo)

    # Verifica se o arquivo CSV existe
    if not os.path.exists(caminho_arquivo_csv):
        return f"Arquivo CSV '{nome_do_arquivo}' não encontrado.", 404

    # Define o tipo de gráfico baseado no parâmetro 'tipo' (padrão: pizza)
    tipo_grafico = request.args.get('tipo', 'pizza')  # 'pizza' ou 'barra'
    # Verifica se o valor "pizza" esta contido no parametro "tipo_grafico" se sim a variavel "pizza" recebe o valor "True"
    pizza = tipo_grafico == "pizza"

    # Chama a função plotar_grafico para gerar o gráfico
    from app.analisar_csv import plotar_grafico
    img = plotar_grafico(caminho_arquivo_csv, pizza=pizza)

    # Retorna a imagem como resposta HTTP
    return Response(img.getvalue(), mimetype='image/png')