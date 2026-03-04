#Peça o peso e a altura do usuário e verifique se ambos são valores maiores que zero
#Se forem válidos,calcule e mostre o IMC. Caso contrário, informe que os valores são inválidos.
peso = float (input ("Digite o seu peso: "))
altura = float (input ("Digite a sua altura: "))
imc = float (peso / (altura*altura))
if peso > 0 and altura > 0:
  print (f"O valor do seu imc é {imc:.2f}")
else:
  print (f"Os valores digitados ou o valor digitado é inválido.")
