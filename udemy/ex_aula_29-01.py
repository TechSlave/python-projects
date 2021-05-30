"""
Faça um programa que peça oa usuário um inteiro, informe se o numero é par ou impar. Caso o usuário não digite um
inteiro, informe que não é um inteiro.
"""
import re


def is_float(val):
    if isinstance(val, float):
        return True
    if re.search(r'^-?[0-9]+\.[0-9]+$', val):
        return True
    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^-?[0-9]+$', val):
        return True
    return False


def is_number(val):
    return is_int(val) or is_float(val)


num = input("Digite um número inteiro: ")
if is_int(num):
    num = int(num)
    if (num % 2) == 0:
        print("Número par")
    else:
        print("Número Ímpar")
else:
    print("Não é um número inteiro")
