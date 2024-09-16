import webbrowser, sys

if len(sys.argv) > 1    :
    adress = ' '.join(sys.argv[1:])
else:
    adress = input("Digite o endereço que deseja abrir no Google Maps: ")
webbrowser.open('https://www.google.com/maps/place/' + adress)


#Exemplo de rodar python Adress.py "870 Valencia St, San Francisco, CA 94110"