##Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente. 
nota1 = int (input("Digite a primeira nota: "))
nota2 = int (input("Digite a segunda nota: "))
somador = 0
i = 0
while 0 > nota1 or nota1 > 10:
    print("Nota inválida! Digite um valor entre 0 e 10.")
    nota1 = int (input("Digite a primeira nota novamente: "))
while 0 > nota2 or nota2 > 10:
    print("Nota inválida! Digite um valor entre 0 e 10")
    nota1 = int (input("Digite a segunda nota novamente: "))
somador = somador + nota1 + nota2
media = somador / (i + 2)
print(f"A media do aluno é {media}")

