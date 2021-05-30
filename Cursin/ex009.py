# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

num = int(input("Digite o número: "))

# for i=0; i<10; i++
print("-"*12)
for i in range(11):
    print("{} x {:2} = {}".format(num, i, num*i))
print("-"*12)