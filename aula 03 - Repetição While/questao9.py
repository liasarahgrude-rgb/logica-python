#Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence (Q1, Q2, Q3 ou Q4). O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma). 
x = int(input("Digite o valor da coordenada x: "))
y = int(input("Digite o valor da coordenada y: "))
while x != 0 or y != 0:
    if x > 0 and y > 0:
        print(f"O ponto pertence ao 1 quadrante!")
        break 
    elif y > 0 and x < 0:
        print("O ponto pertence ao 2 quadrante!") 
        break
    elif x < 0 and y < 0:
        print("O ponto pertence ao 3 quadrante!") 
        break
    elif x > 0 and y < 0:
        print("O ponto pertence ao 4 quadrante")
        break
print("")
         
