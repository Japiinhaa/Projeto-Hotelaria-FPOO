#menu
from classe2 import *
import os
clientes = {}
cliente = []
quartos = ['1- Apartamento simples', '2- Apartamento simples casal', '3- Apartamento simples casal', '4- Apartamento simples', ]


def set_cliente():

        nome = input('Digite seu nome: ')
        cpf = input('Digite o seu CPF: ')
        quarto = 0
        cliente = [nome, cpf, quarto]
        clientes.append(cliente)
        print('Cliente cadastrado com sucesso!')
        os.system('pause')
        os.system('cls')


def buscarcliente():
        nome = input('Digite o nome do cliente que deseja buscar: ')
        for cliente in clientes:
            if cliente[0] == nome:
                print(f'Nome: {cliente[0]} \nCPF: {cliente[1]}\nQuarto {cliente[2]}')
                return
        print('Cliente não encontrado.')
        os.system('pause')
        os.system('cls')

def buscarespecificações():
        n_quarto = int(input('Digite o numero do quarto que deseja buscar: '))
        for n_quarto in quartos:
            if cliente[0] == n_quarto:
                print(f'Nome: {cliente[0]} \nCPF: {cliente[1]}\nQuarto {cliente[2]}')
                return
        print('Cliente não encontrado.')
        os.system('pause')
        os.system('cls')





def main(opcoes):
    match opcoes:
        case 1:
            print('Você selecionou a opção de Adicionar Buscar por espesificações!')
            buscarespecificações()
            os.system("cls")
        case 2:
            print('Você selecionou a opção de Listar quartos!')
            ()
            os.system("cls")
        case 3:
            print('Você selecionou a opção de Listar quartos livres!')
            ()
            os.system("cls")
        case 4:
              os.system("cls")
              print('Você selecionou a opção de Listar clientes!')
            ()

        case :
              print('Opção inválida!')
