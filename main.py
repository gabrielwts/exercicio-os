import random
import os

# Listar arquivos no diretório atual
arquivos = os.listdir()
print("Arquivos no diretório atual:", arquivos)

# Criar uma nova pasta e navegar até ela
nova_pasta = "Projetos"
os.mkdir(nova_pasta)
os.chdir(nova_pasta)
print(f"Agora estamos em: {os.getcwd()}")

# Criação de uma pasta se não existir
os.makedirs("Projetos", exist_ok=True)

for i in range(5):
    # Cria um nome com o número aleatório
    nome_arquivo = f"arquivo{random.randint(1, 99)}.txt"
    caminho_arquivo = os.path.join("Projetos", nome_arquivo)

    try:
        #escreve dentro do arquivo novo
        with open(caminho_arquivo, 'w') as f:
            f.write("OI")
        print("Criado", nome_arquivo)
    except:
        print("deu Erro")