##O programa deve ler um valor inteiro X indefinidas vezes. (O programa irá parar quando o valor de X for igual a 0). Para cada X lido, imprima a soma dos 5 pares consecutivos a partir de X, inclusive o X, se for par. Se o valor de entrada for 4, por exemplo, a saída deve ser 40, que é o resultado da operação: 4+6+8+10+12, enquanto que se o valor de entrada for 11, por exempo, a saída deve ser 80, que é a soma de 12+14+16+18+20.
valor = int (input("Digite um valor: "))
totalsoma = 0
while valor != 0:
    if valor % 2 == 0:
        totalsoma = 0
        for num in range(valor, valor + 10, 2): # Indo até +10 para incluir o +8
            totalsoma += num 
        print(totalsoma) # Fora do for, mas dentro do if
    elif valor % 2 != 0:
        totalsoma = 0
        for num in range(valor+1, valor+11, 2): 
            totalsoma += num 
        print({totalsoma})
    valor = int (input("Digite um valor: "))