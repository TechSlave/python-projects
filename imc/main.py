# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import os
peso = 0
altura = 0
#cmd = 'xdg-open https://www.smartfit.com.br/'
#cmd2 = 'xdg-open https://www.mcdonalds.com.br'
print("Calculadora de IMC")
peso = float(input("Digite o peso (ex 68): "))
altura = float(input("Digite a altura (ex 1.70): "))
imc = peso / (altura * altura)
print("Seu imc é {:.2f}".format(imc))
if imc < 18.5:
    print("Você é Magro")
#    os.system(cmd2)
if imc >= 18.5 and imc < 25:
    print("Você é Normal")
if imc >= 25 and imc < 30:
    print("Você está com Sobrepeso")
if imc >= 30 and imc < 40:
    print("Você tá gordão")
if imc >= 40:
    print("Você está gravemente obeso")
#    os.system(cmd)
