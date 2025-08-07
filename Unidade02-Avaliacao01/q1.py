
banco_dados = {}

#Função que valida o CPF durante o cadastro do CPF
def cpf_valido (cpf):
    if type(cpf) != str:
        return False
    cpf = cpf.replace(".", "").replace("-", "")
    if cpf.isdecimal() == False:
        return False
    if len(cpf) != 11:
        return False
    
    soma = 0
    for pos in range (9):
        soma += int(cpf[pos]) * (10 - pos)
    dv1 = 11 - soma % 11
    if dv1 >= 10: dv1 = 0
        
    if dv1 != int(cpf[9]):
        return False
    
    soma = 0
    for pos in range (10):
        soma += int(cpf[pos]) * (11 - pos)
    dv2 = 11 - soma % 11
    if dv2 >= 10: dv2 = 0
        
    if dv2 != int(cpf[10]):
        return False
    
    return True

#Função que cadrasta o CPF
def cadastrar_cpf():
    cpf = input("Digite o CPF (somente números): ")
    print ("CPF é valido:", cpf_valido(cpf))
    if cpf_valido((cpf)) == False:
        print("CPF inválido!")
        return
    if cpf in banco_dados:
        print("CPF já cadastrado.")
        print() #Esses prints extras estão em todas as funções e são para pular linhas, para deixar o programa mais organizado e fácil de ler
    else:
        banco_dados[cpf] = []
        print("CPF cadastrado com sucesso.")
        print()

#Função que adicionar um endereço MAC a um CPF
def adicionar_mac():
    cpf = input("Digite o CPF: ")
    if cpf not in banco_dados:
        print("CPF não cadastrado.")
        print()
        return
    mac = input("Digite o endereço MAC: ")
    if mac in banco_dados[cpf]:
        print("MAC já vinculado a este CPF.")
        print()
    else:
        banco_dados[cpf].append(mac)
        print("MAC vinculado com sucesso.")
        print()

#Função que remove um endereço MAC a um CPF
def remover_mac():
    cpf = input("Digite o CPF: ")
    if cpf not in banco_dados:
        print("CPF não cadastrado.")
        print()
        return
    mac = input("Digite o endereço MAC a remover: ")
    if mac in banco_dados[cpf]:
        banco_dados[cpf].remove(mac)
        print("MAC removido com sucesso.")
        print()
    else:
        print("MAC não encontrado para este CPF.")
        print()

#Função que remove um CPF do banco de dados (caso ele não tenha um MAC associado)
def remover_cpf():
    cpf = input("Digite o CPF: ")
    if cpf in banco_dados:
        if banco_dados[cpf]:
            print("CPF possui MACs vinculados. Não pode ser removido.")
            print()
        else:
            del banco_dados[cpf]
            print("CPF removido com sucesso.")
            print()
    else:
        print("CPF não encontrado.")
        print()

#Função que lista os CPFs cadastrados no banco de dados
def listar_cpfs():
    if not banco_dados:
        print("CPFs não cadastrados.")
        print()
    else:
        for cpf in banco_dados:
            print(f"{cpf}")
        print()

#Função que lista os MACs associados a um CPF
def listar_macs():
    cpf = input("Digite o CPF: ")
    if cpf in banco_dados:
        if banco_dados[cpf]:
            print(f"MACs vinculados ao CPF {cpf}:")
            for mac in banco_dados[cpf]:
                print(f"{mac}")
            print()
        else:
            print("Nenhum MAC vinculado a este CPF.")
            print()
    else:
        print("CPF não encontrado.")
        print()

#Função que salva o banco de dados em arquivos, com um nome de sua escolha
def salvar_arquivo():
    nome = input("Digite o nome do arquivo para salvar: ")
    fd = open(nome, 'w')
    fd.write(str(banco_dados)) #Transformando o dicionário em uma string, para que possa criar o código
    fd.close()
    print(f"Banco de dados salvo em {nome}.")
    print()

#Função que carrega o arquivo contendo o banco de dados
def carregar_arquivo():
    global banco_dados
    nome = input("Digite o nome do arquivo para carregar: ")
    try:
        fd = open(nome, 'r')
        fd.close()
        print("Banco de dados carregado com sucesso.")
        print()
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        print()

#Função para iniciar o menu
def menu():
    while True:
        print("Digite 'a' para cadastrar um CPF")
        print("Digite 'b' para adicionar um endereço MAC a um CPF")
        print("Digite 'c' para remover um endereço MAC de um CPF")
        print("Digite 'd' para remover o CPF (se não tiver um MACs associado)")
        print("Digite 'e' para listar os CPFs cadastrados")
        print("Digite 'f' para listar os MACs vinculados a um CPF")
        print("Digite 'g' para salvar o banco de dados em arquivo")
        print("Digite 'h' para carregar o banco de dados de um arquivo")
        print("Digite 's' para encerrar esse programa")

        #Esse input irá informar qual função será chamada, de acordo com o que o usuário digite.
        opcao = input("Escolha uma opção: ").lower()

        if opcao == 'a':
            cadastrar_cpf()
        elif opcao == 'b':
            adicionar_mac()
        elif opcao == 'c':
            remover_mac()
        elif opcao == 'd':
            remover_cpf()
        elif opcao == 'e':
            listar_cpfs()
        elif opcao == 'f':
            listar_macs()
        elif opcao == 'g':
            salvar_arquivo()
        elif opcao == 'h':
            carregar_arquivo()
        elif opcao == 's':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida.") #Se o usuário digitar uma letra que não corresponde a alguma opção
            print()

#Chamada da função para iniciar o menu

menu()

