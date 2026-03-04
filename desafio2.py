##Crie um sistema de login simples que peça o nome do usuário. 
# Permita o acesso apenas se o nome for “admin”. Caso contrário, mostre que o usuário é inválido.
nome = input ("Digite o nome do usuário: ")
if nome == "admin":
    print (f"Acesso permitido")
else : 
    print(f"O usuário é inaválido")