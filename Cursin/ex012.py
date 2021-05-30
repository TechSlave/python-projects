# Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor = float(input("Digite o preço do produto (R$): "))
resultado = (valor-(valor*0.05))
print("O valor R${} com desconto de 5% é: R${}".format(int(valor), int(resultado)))