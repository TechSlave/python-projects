"""
https://www.practicepython.org

Create a program that asks the user to enter their name and their age. Print out a message addressed to them that 
tells them the year that they will turn 100 years old. 

Extras:

1. Add on to the previous program by asking the user for another number and printing out that many copies of the
previous message. (Hint: order of operations exists in Python)
.2 Print out that many copies of the previous message on
separate lines. (Hint: the string "\n is the same as pressing the ENTER button) 

"""
from datetime import date

name = input("Digite seu nome: ")
age = int(input("Digite sua idade: "))
repeat = int(input("Deseja repetir quantas vezes? (sim é estranho mas é o exercício): "))
yearnow = date.today()
hundred = (yearnow.year + 100) - age

print("{}, você fará 100 anos em {}\n".format(name, hundred) * repeat)
