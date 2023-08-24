clientes = {}
chave = 0
chave_disponivel = 1

cliente = []
quartos = ['1- Apartamento simples', '2- Apartamento simples casal', '3- Apartamento simples casal', '4- Apartamento duplo', '5- Apartamento simples', '6- Apartamento duplo casal', '7- Apartamento duplo casal','8- Apartamento duplo', '9- Apartamento_master', '10- Apartamento_master', '11- Apartamento_Luxo', '12- Apartamento_Luxo' ]
import os




class Hotel():
    def __init__(self, nome, cpf, quarto):
        self.nome = []
        self.cpf = []
        self.quarto = []
        
    def pesquisar_quarto():
        seleçao_ = input ("")

    def set_cliente():

        nome = input('Digite seu nome: ')
        cpf = input('Digite o seu CPF: ')
        quarto = 0
        
        if chave == chave_disponivel:
            cliente = [nome, cpf, quarto]
            clientes.append(cliente)
            print('Apartamento reservado com sucesso!')
        os.system('pause')
        os.system('cls')
    

class Quartos(Hotel):
    def __init__(self, capacidade, preco, itens, tamanho):
        self.capacidade = []
        self.preco = []
        self.itens = []
        self.tamanho = []
        

    def listar_especificações():
        print ('Capacidade: {capacidade}')



#    def listar_quartos():

    




class AP_luxo(Quartos):
    def especificações():
        capacidade = "4"
        preço = "3600"
        itens = 'Cama king size casal\nTV 8k 55"\nVista direta pro mar \nDuas vagas para garagem \nArea gourmet \nDuas suites\n sala de estar grande\n cozinha e com lavanderia com espaço para cobertura '
        tamanho = '220m²'

       
class AP_master(Quartos):
    def especificações():
        capacidade = "6"
        preço = "1300"
        itens = '2 beliches e uma cama de casal simples \nventilador de teto nos quartos \nVista direta pro mar \nDuas vagas para garagem\numa suite\numa sala com mesa de estar\n uma cozinha pequena com lavanderia'
        tamanho = '170m²'        


class AP_simples(Quartos):
    def especificações():
        capacidade = "2"
        preço = "350"
        itens = 'uma beliche \nTV 1080 40" \nVista direta pro mar \nDuas vagas para garagem \nArea gourmet \nDuas suites'
        tamanho = '50m²'   


class AP_simples_casal(Quartos):
    def especificações():
        capacidade = "4"
        preço = "500"
        itens = 'Cama king size \nTV 8k 55" \nVista direta pro mar \nDuas vagas para garagem \nArea gourmet \nDuas suites'
        tamanho = '90m²'


class AP_duplo(Quartos):
    def especificações():
        capacidade = "4"
        preço = "680"
        itens = 'Cama king size \nTV 8k 55" \nVista direta pro mar \nDuas vagas para garagem \nArea gourmet \nDuas suites'
        tamanho = '70m²'
        
class AP_duplo_casal(Quartos):
    def especificações():
        capacidade = "2"
        preço = "800"
        itens = 'Cama king size \nTV 8k 55" \nVista direta pro mar \nDuas vagas para garagem \nArea gourmet \nDuas suites'
        tamanho = '111m²'