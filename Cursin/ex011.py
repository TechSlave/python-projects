# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
# 2 Litros por metro quadrado
print(("#"*10)+" Calculadora de Pintura "+("#"*10))

altura = float(input("Altura (m): "))
largura = float(input("Largura (m): "))
area = altura*largura
print("\nDimensões da parede:\nAltura: {}m\nLargura: {}m\nÁrea: {}m²".format(altura, largura, area))
print("\nSão necessárias {} latas de tinta.".format(area/2))

print("#"*44)
