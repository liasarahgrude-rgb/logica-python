##Um posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes. Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma: 1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código (até que seja válido). O programa será encerrado quando o código informado for o número 4, devendo então mostrar a mensagem "MUITO OBRIGADO", bem como as quantidades de cada combustível. 
combustivel = int(input("Qual tipo de combustivel abastecido: \n1. Álcool\n2. Gasolina\n3. Diesel\n4. Fim\n"))
conta = 0
contg = 0
contd = 0
while combustivel != 4:
    if combustivel == 1:
        conta = conta + 1
    elif combustivel == 2:
        contg = contg + 1
    elif combustivel == 3:
        contd = contd + 1
    elif combustivel < 1 or combustivel > 4:
        print("Código inválido! Tente novamente.")
    combustivel = int(input("Digite um numero entre 1-4 para informar o tipo de combustivel abastecido: \n1. Álcool\n2. Gasolina\n3. Diesel\n4. Fim\n"))# Este input acontece SEMPRE, não importa se foi 1, 2 ou 3
print("MUITO OBRIGADO!")
print(f"{conta} pessoas abasteceram com Alcool\n{contg} pessoas abasteceram com gasolina\n{contd} pessoas abasteceram com diesel")
