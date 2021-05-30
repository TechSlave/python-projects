# Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
# com 15% de aumento.


salario = float(input("Digite o salario (R$): "))
novo_salario = (salario-(salario*0.15))
print("O salario R${} com 15% de aumentou passou a ser de: R${}".format(int(salario), int(novo_salario)))
