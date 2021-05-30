i_menu = 0
i_compra = 0
contador = 1
soma = 0
dados_compra = ""
print("\n  " + "#"*6 + " Calculadora de mercado " + "#"*6)
# divida_antiga = float(input("Digite o valor da dívida anterior: "))
# devedor = input("Digite o Devedor: ")

print("\n" + "="*13 + " Menu Inicial " + "="*13 +
      "\n(1) - Ver anterior"
      "\n(2) - Inserir nova compra"
      "\n(3) - Sair")
option = int(input("Digite a opção: "))

while i_menu < 1:
    if option == 1:
        print("\nCompras anteriores:")
        f = open("mercado.txt", "r")
        print(" " + f.read())
        f.close()
        i_menu = 1
    elif option == 2:
        print("Nova Compra")
        data = input("Digite a data da compra: ")
        comprador = input("Digite quem pagou a compra: ")
        while i_compra < 1:
            resposta = float(input("Digite o valor do item {} ou digite 0 para sair: ".format(contador)))
            if resposta != 0:
                contador = contador+1
                soma = (soma+resposta)
            else:
                i_compra = 1
            dados_compra = ("\nData: {}"
                            "\nComprador: {}"
                            "\nValor total: R${:.2f}"
                            "\n{}"
                            .format(data, comprador, soma, "#"*30))
        print("\nSalvar compra?"
              "\n(1) - Sim"
              "(2) - Não")
        gravar = int(input("Digite a opção: "))
        if gravar == 1:
            print("Salvando compra...")
            f = open("mercado.txt", "a")
            f.write(dados_compra)
            f.close()
            print("Compra Salva!")
            i_menu = 1
    else:
        i_menu = 1
i_menu = 1




