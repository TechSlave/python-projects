import math

angulo = float(input("Digite o Ângulo a ser calculado: "))

sen = math.sin(math.radians(angulo))
print("O ângulo de {} tem o Seno de {:.2f}".format(angulo, sen))

cos = math.cos(math.radians(angulo))
print("O ângulo de {} tem o Cosseno de {:.2f}".format(angulo, cos))

tan = math.tan(math.radians(angulo))
print("O ângulo de {} tem o Seno de {:.2f}".format(angulo, tan))
