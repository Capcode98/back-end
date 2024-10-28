import pandas as pd
import matplotlib.pyplot as plt
import io
import matplotlib
matplotlib.use('Agg')  # Define backend para evitar exibição direta

def plotar_grafico(Arquivo_csv, pizza=True):
    try:
        # Carregando o arquivo CSV
        analise = pd.read_csv(Arquivo_csv)

        # Verifica se as colunas necessárias estão presentes
        if 'curso' not in analise.columns or 'nota da materia' not in analise.columns:
            raise ValueError("O arquivo CSV deve conter as colunas 'curso' e 'nota da materia'.")

        # Calculando a média das notas por curso
        notas_medias_curso = (
            analise.groupby('curso')['nota da materia']
            .mean()
            .reset_index()
            .round(2)
        )

        # Renomeando as colunas para exibição
        notas_medias_curso.columns = ['Curso', 'Média das Notas']

        # Criação do buffer para armazenar a imagem
        img = io.BytesIO()

        if pizza:
            # Gráfico de Pizza
            plt.figure(figsize=(10, 6))  # Ajuste de tamanho para melhor visualização
            plt.pie(
                notas_medias_curso['Média das Notas'],
                labels=notas_medias_curso['Curso'],
                autopct='%1.1f%%',
                startangle=140,
                colors=plt.cm.Paired(range(len(notas_medias_curso)))
            )
            plt.title('Distribuição das Médias das Notas por Curso', fontsize=14)

        else:
            # Gráfico de Barras
            plt.figure(figsize=(8, 5))
            plt.bar(
                notas_medias_curso['Curso'],
                notas_medias_curso['Média das Notas'],
                color='skyblue'
            )
            plt.xlabel('Curso', fontsize=12)
            plt.ylabel('Média das Notas', fontsize=12)
            plt.title('Média das Notas por Curso', fontsize=14)
            plt.xticks(rotation=45, ha='right')  # Ajuste para os rótulos do eixo X
            plt.tight_layout()  # Garante que tudo caiba na figura

        # Salva o gráfico no buffer como PNG
        plt.savefig(img, format='png')
        img.seek(0)  # Volta para o início do buffer
        plt.close()  # Fecha o gráfico para liberar memória

        return img  # Retorna o buffer com a imagem

    except Exception as e:
        # Tratamento de erros
        print(f"Erro ao gerar gráfico: {str(e)}")
        raise
