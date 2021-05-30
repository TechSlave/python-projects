# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor = int(input("Digite o valor em Metros: "))
dm = valor * 10
cm = valor * 100
mm = valor * 1000
####
dam = valor / 10
hm = valor / 100
km = valor / 1000
print("{}m equivalem a: \n{}dm\n{}cm\n{}m\n============\n{}dam\n{}hm\n{}km".format(valor, dm, cm, mm, dam, hm, km))
