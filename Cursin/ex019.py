import random

aluno1 = input("Primeiro Aluno: ")
aluno2 = input("Segundo Aluno: ")
aluno3 = input("Terceiro Aluno: ")
aluno4 = input("Quarto Aluno: ")

print("Aluno escolhido: {}".format(random.choice([aluno1, aluno2, aluno3, aluno4])))
