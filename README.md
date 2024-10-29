# PROJETO BACK-END
## DESCRIÇÃO DO PROJETO
- #### Este projeto foi proposto para a Disciplina PROJETO DE DESENVOLVIMENTO WEB BACK END - 5º/6° Período.
### PROJETO DE ANALISE DE DADOS ESTUDANTIS
- #### Esse projeto foi e está sendo desenvolvido pelos alunos do grupo 2 de Ciências da Computação da UNIFESO.

    #### EQUIPE 2

    - ##### PO: *[Lucas Rodrigues Lourenço](https://www.linkedin.com/in/lucas-rodrigues-44a707282/)*
    - ##### ScrumMaster: *[Lucas do Canto de Carvalho](https://www.linkedin.com/in/lucas-do-canto-de-carvalho-7bb2a4279/)*
    - ##### Dev-Back_end: *[João Luis Berute](https://www.linkedin.com/in/joao-luis-berute-ribeiro/)*
    - ##### Dev-Front_end1: *[Marcos Vinicius da costa silva](https://www.linkedin.com/in/marcos-vinicius-costa-silva-853ab2285/)*
    - ##### Dev-Front_end2: *[Pedro Henrique SantAna de Souza](https://www.linkedin.com/in/pedro-henrique-453b9b26a/)*
    - ##### QA: *[Diego Moreira da Silva](https://www.linkedin.com/in/diego-moreira-387a5b335/)*

#
# TECNOLOGIAS UTILIZADAS
- # BACK-END
    - ## Python 3.12.2
        Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.
        - ### Flask
            Flask é um pequeno framework web escrito em Python. É classificado como um microframework porque não requer ferramentas ou bibliotecas particulares, mantendo um núcleo simples, porém, extensível.
        - ### Pandas
            Pandas é uma biblioteca de software criada para a linguagem Python para manipulação e análise de dados. Em particular, oferece estruturas e operações para manipular tabelas numéricas e séries temporais.
        - ### Matplotlib
            Matplotlib é uma biblioteca de software para criação de gráficos e visualizações de dados em geral, feita para e da linguagem de programação Python.
        - ### PyJWT
            PyJWT é uma biblioteca Python que permite codificar e decodificar JSON Web Tokens (JWT). JWT é um padrão aberto da indústria ( RFC 7519 ) para representar reivindicações com segurança entre duas partes.

    - ## MySQL 
        O MySQL é um sistema de gerenciamento de banco de dados, que utiliza a linguagem SQL como interface. É atualmente um dos sistemas de gerenciamento de bancos de dados mais populares da Oracle Corporation, com mais de 10 milhões de instalações pelo mundo.
#

### Funcionalidades
- Criação de usuários
- Leitura de usuários
- Atualização de usuários
- Exclusão de usuários

### Requisitos Básicos
- [python 3.12.2](https://www.python.org/downloads/)
- [mysql](https://www.mysql.com/downloads/)
- [git](https://git-scm.com/downloads)

### Instalação
#### Passo 1 - Clone o repositorio 
- Abra o terminal do windows e escreva na barra de pesquisa o seguinte comando:

        CMD 
    ou 

        Prompt de Comando

- Vá para a pasta aonde você pretende fazer o download deste repositório com o seguinte comando:

        cd "Nome_da_pasta"

- Clone o projeto com o seguinte comando:

        git clone https://github.com/Capcode98/back-end.git
    
- Crie um ambiente virtual Python com o seguinte comando:

        py -m venv .venv

- Ative o seu ambiente virtual com o seguinte comando:

        ./.venv/Scripts/Activate

- Instale as dependências necessarias do projeto, com o seguinte comando:

        pip install -r requirements.txt 

- Vá para dentro do projeto com o seguinte comando:

        cd (funcionando)Exemplo_Funcional_de_Upload_de_Arquivos

- Modifique o arquivo .flaskenv(Model) e o renomeie para .flaskenv com o seguinte comando:

        mv .flaskenv(Model) .flaskenv

- Abra o aquivo .flaskenv com seu editor de código e modifique a variavel de ambiente FLASK_RUN_PORT assocoando a ela algum valor inteiro:

        FLASK_RUN_PORT = 1234 (Exemplo)

- Rode o projeto com o seguinte comando:

        py -m flask run