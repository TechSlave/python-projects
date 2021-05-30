"""
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e
todas as informações possíveis sobre ele.
"""

entrada = input("Digite algo: ")

print("O tipo primitivo desse valor é: {}".format(type(entrada)))
print("Só tem espaços? {}".format(entrada.isspace()))
print("É um número? {}".format(entrada.isnumeric()))
print("É alfabético? {}".format(entrada.isalpha()))
print("É alfanumérico? {}".format(entrada.isalnum()))
print("Está em maiúsculas? {}".format(entrada.isupper()))
print("Está em minúsculas? {}".format(entrada.islower()))
print("Está capitalizada? {}".format(entrada.istitle()))
