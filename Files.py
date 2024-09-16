def criar_arquivo(nome_arquivo, conteudo):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(conteudo)
        print(f"Arquivo '{nome_arquivo}' criado com sucesso.")
    except Exception as e:
        print(f"Erro ao criar o arquivo: {e}")

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
        return conteudo
    except FileNotFoundError:
        return f"Arquivo '{nome_arquivo}' não encontrado."
    except Exception as e:
        return f"Erro ao ler o arquivo: {e}"

def alterar_arquivo(nome_arquivo, novo_conteudo):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(novo_conteudo)
        print(f"Arquivo '{nome_arquivo}' alterado com sucesso.")
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Erro ao alterar o arquivo: {e}")

# Exemplo de uso
nome_arquivo = 'exemplo.txt'
conteudo_inicial = 'Este é o conteúdo inicial do arquivo.'
novo_conteudo = 'Este é o novo conteúdo do arquivo.'

# Criar o arquivo
criar_arquivo(nome_arquivo, conteudo_inicial)

# Ler o arquivo
print("Conteúdo do arquivo:", ler_arquivo(nome_arquivo))

# Alterar o arquivo
alterar_arquivo(nome_arquivo, novo_conteudo)

# Ler o arquivo novamente
print("Conteúdo do arquivo após alteração:", ler_arquivo(nome_arquivo))