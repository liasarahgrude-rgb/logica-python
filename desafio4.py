#Peça a nota e a quantidade de faltas do aluno.
#Mostre “Aprovado” se a nota for maior ou igual a 7 ou se a quantidade de faltas for menor ou igual a 5.
#Caso contrário, mostre “Reprovado”.
nota = float (input ("Digite sua nota: "))
qfalta = int (input ("Digite a sua quantidade de faltas: "))
if nota >= 7 or qfalta <= 5 :
    print(f"Aprovado!")
else : 
    print(f"Reprovado!")