##1. Peça a cidade do usuário e permita o acesso apenas se a cidade for “Fortaleza”. 
# Caso contrário, mostre que o acesso foi negado.
cidade = input ("Digite a sua cidade: ")
if cidade == "Fortaleza" or cidade == "fortaleza":
    print(f"Acesso permitido!")
else: 
    print(f"Acesso negado!")