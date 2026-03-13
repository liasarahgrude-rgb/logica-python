##O programa deve ler um valor inteiro X indefinidas vezes. (O programa irá parar quando o valor de X for igual a 0). Para cada X lido, imprima a soma dos 5 pares consecutivos a partir de X, inclusive o X, se for par. Se o valor de entrada for 4, por exemplo, a saída deve ser 40, que é o resultado da operação: 4+6+8+10+12, enquanto que se o valor de entrada for 11, por exempo, a saída deve ser 80, que é a soma de 12+14+16+18+20.
valor = int (input("Digite um valor: "))
while valor != 0:
    if valor % 2 == 0:
        somapar = valor + (valor+2) + (valor+4) + (valor+6) + (valor+8)
        print(f"{somapar}")
    elif valor % 2 != 0:
        somaimpar = (valor+1) + (valor+3) + (valor+5) + (valor+7) + (valor+9)
        print(f"{somaimpar}")
    valor = int (input("Digite um valor: "))



    
