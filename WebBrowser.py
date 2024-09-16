import webbrowser
import sys
#import pyperclip

def abrir_site():
    # Verifica se o usuário passou um argumento via linha de comando
    if len(sys.argv) > 1:
        site = sys.argv[1]
    else:
        # Pede ao usuário para inserir a URL
        site = input("Digite a URL do site que você deseja abrir (ex: https://www.google.com): ")

    # Abre o site no navegador padrão
    if not site.startswith('http'):
        site = 'http://' + site  # Adiciona http se o usuário não tiver incluído
    webbrowser.open(site)
    print(f"Abrindo o site: {site}")

# Executa a função para abrir o site
abrir_site()
