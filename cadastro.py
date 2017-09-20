print("Nome")
nome = input("Digite o seu nome: ")
print("Endereço")
rua = input("Digite o nome da rua: ")
cep = int(input("Digite o número do CEP: "))
bairro = input("Digite o nome do bairro: ")
estado = input("Digite o nome do estado: ")
print("Telefone")
tel = int(input("Digite o número do telefone: "))
perg = input("Deseja inserir um novo dado? (Sim) ou (Não)")


arq = open("cadastro.txt", "a")
text = "Nome: {} \nEndereço: {}, {}, {}, {} \nTelefone: {}\n".format(nome, rua, cep, bairro, estado, tel)
arq.write(text)
    
while perg == "Sim":
    print("Nome")
    nomew = input("Digite o seu nome: ")
    print("Endereço")
    rua = input("Digite o nome da rua: ")
    cep = int(input("Digite o número do CEP: "))
    bairro = input("Digite o nome do bairro: ")
    estado = input("Digite o nome do estado: ")
    print("Telefone")
    tel = int(input("Digite o número do telefone: "))
    perg = input("Deseja inserir um novo dado? (Sim) ou (Não)")
    c = input("Deseja fazer uma consulta? (Sim) ou (Não)")
    text = "Nome: {} \nEndereço: {}, {}, {}, {} \nTelefone: {}\n".format(nomew, rua, cep, bairro, estado, tel)
    arq.write(text)

    arq = open("cadastro.txt", "a")
    if c == "Sim":
        cons = input("Digite o nome que deseja consultar? ")
        if cons == nome or cons == nomew:
            print(text)



