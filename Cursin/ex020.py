import random

aluno1 = input("Primeiro Aluno: ")
aluno2 = input("Segundo Aluno: ")
aluno3 = input("Terceiro Aluno: ")
aluno4 = input("Quarto Aluno: ")
alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(alunos)
print("Aluno escolhido: {}".format(alunos))
