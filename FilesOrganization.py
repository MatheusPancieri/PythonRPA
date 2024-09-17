import os
from tkinter.filedialog import askdirectory

# Achar o caminho da pasta
caminho = askdirectory(title = "Selecione uma pasta")
print (caminho)

# Listar todos os arquivos dentro da pasta
lista_arquivo = os.listdir(caminho)
print (lista_arquivo)

# Definir os tipos que cada pasta vai alocar
locais = {
    "Imagens" : [".png", ".jpg", ".bmp"],
    "MicrosoftDocs" : [".pptx", ".docx", ".xlsx"],
    "Pdfs" : [".pdf"],
    "Txt" : [".txt"],
    "Csv" : [".csv"],
}

for arquivo in lista_arquivo:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")