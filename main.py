from classe2 import *
from algo import *
import os


if __name__ == '__main__':
    while True:
        try:  
            print("Escolha uma opção: \n 1. Buscar por espesificações \n 2. Listar quartos \n 3. Listar quartos livres \n 4. Listar clientes")
            opcoes = int(input('Escolha uma dessa opções:'))
            os.system("cls")
            main(opcoes)

        except Exception as erro:
            os.system("cls")
            print('Erro! Digite apenas números inteiros.')
            
