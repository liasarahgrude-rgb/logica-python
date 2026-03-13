##Problema "tabuada" Ler um número inteiro N, daí mostrar na tela a tabuada de N para 1 a 10.
num = int (input("Digite um número inteiro: "))
print(f"Tabuada do {num}:")
for num2 in range(1, 11):
    num3 = num2 * num
    print(f"{num} x {num2} = {num3}")
