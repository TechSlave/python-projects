from datetime import date

nome = input("Nome: ")
idade = int(input("Idade: "))
altura = float(input("Altura: "))
peso = float(input("Peso: "))
ano_atual = date.today().year

nascimento = ano_atual - idade
imc = peso / (altura*altura)

print("Nome: {}\n"
      "Idade: {}\n"
      "Altura: {}m\n"
      "Peso: {:.0f}Kg\n"
      "Ano de Nascimento: {}\n"
      "IMC: {:.2f}".format(nome, idade, altura, peso, nascimento, imc))
