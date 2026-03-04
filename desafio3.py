##Peça a idade e a cidade do usuário. 
# Permita o acesso apenas se ele tiver 18 anos ou mais e morar em “Fortaleza”. Caso contrário, mostre “Acesso negado”.
idade = int(input("Digite sua idade: "))
cidade = input ("Digite sua cidade: ")
if idade >= 18 and cidade == "Fortaleza" or cidade == "fortaleza":
    print(f"Acesso permitido!")
else : 
    print(f"Acesso negado!")