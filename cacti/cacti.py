# -*- coding: utf-8 -*-
import os


# Classe de cores do Terminal
class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Função para inserir cor no texto
def colors(text, color, bold='false'):
    out = ""
    if color == "red":
        out = Bcolors.FAIL + text + Bcolors.ENDC
    elif color == "blue":
        out = Bcolors.OKBLUE + text + Bcolors.ENDC
    elif color == "green":
        out = Bcolors.OKGREEN + text + Bcolors.ENDC
    elif color == "yellow":
        out = Bcolors.WARNING + text + Bcolors.ENDC
    elif color == "pink":
        out = Bcolors.HEADER + text + Bcolors.ENDC

    if bold == 'true':
        return Bcolors.BOLD + out
    return out


# Constantes
cli = '/var/www/html/cacti/cli/'
os.system('clear')
# ASCII do Cacto
print(colors(
    ",*-.\n                   |  |\n               ,.  |  |\n               | |_|  | ,.\n               `---.  |_| "
    "|\n                   |  .--`\n                   |  |\n                   |  | ",
    'green', 'false'))
print(colors("Pamcary Tech Team - Gerenciamento de Hosts Cacti", "red", "true"))
print(colors("\nSelecione a opção.", "red", "false"))
print(colors("\n1 - Inserir hosts\n2 - Remover hosts", "green", "false"))
decision1 = input(colors("\nOpção: ", 'blue', 'true'))
os.system('clear')
if decision1 == "1":
    print(colors(
        "                   ,*-.\n                   |  |\n               ,.  |  |\n               | |_|  | ,.\n               `---.  |_| |\n                   |  .--`\n                   |  |\n                   |  | ",
        'green', 'false'))
    print(colors("Pamcary Tech Team - Gerenciamento de Hosts Cacti", "red", "true"))
    print(colors("\n    Inserção de hosts", "blue", "true"))
    print(colors("\n    Selecione o SO dos hosts a serem adicionados.", "red", "false"))
    print(colors(
        "\n    O arquivo deve estar neste diretório e se chamar, respectivamente, \"linux.txt\" ou \"windows.txt\"",
        "yellow", "false"))
    print(colors("\n    1 - Linux\n    2 - Windows", "green", "false"))
    decision = input(colors("\n    Opção: ", 'blue', 'true'))
    if decision == "1":
        template = 7
        os.system('clear')
        print(colors('\n\n      Inserindo máquinas Linux no banco do Cacti', 'green', 'false'))
        file = open('linux.txt', 'r')
    elif decision == "2":
        template = 6
        os.system('clear')
        print(colors('\n\n      Inserindo máquinas Windows no banco do Cacti', 'green', 'false'))
        file = open('windows.txt', 'r')
    site = 0
    for line in file:
        fields = line.split(';')
        ip = fields[0].rstrip()
        description = fields[1].rstrip()
        if "192.168.128" in ip or "200.192." in ip:
            print(
                colors('\nDescriçao: ', 'red') +
                colors(description, 'blue') +
                colors(' IP: ', 'red') +
                colors(ip, 'blue') +
                colors(' Site: ', 'red'),
                colors('UOl Diveo', 'blue')
            )
            site = 1
        else:
            print(
                colors('\nDescriçao: ', 'red') +
                colors(description, 'blue') +
                colors(' IP: ', 'red') +
                colors(ip, 'blue') +
                colors(' Site: ', 'red'),
                colors('DC Pamcary', 'blue')
            )
            site = 2
        cmd = f'php {cli}add_device.php --description={description} --ip={ip} --template={template} --site={site}'
        #    decision = input("Comando:"+cmd+"\nDeseja continuar (y)")
        #    if decision == "y":
        #        os.system('clear')
        # test = description.split()
        if "gps-" in description and template == 7:
            print("Ignorando host: " + description)
        elif "pam-" in description and template == 7:
            print("Ignorando host: " + description)
        else:
            print('\n' + cmd + '\n')
            os.system(cmd)
        # print(cmd)
    file.close()
    # os.system('clear')
    print(colors('\n\n      Máquinas inseridas.\n\n', 'green', 'true'))
if decision1 == "2":
    print(colors(
        "                   ,*-.\n                   |  |\n               ,.  |  |\n               | |_|  | ,.\n               `---.  |_| |\n                   |  .--`\n                   |  |\n                   |  | ",
        'green', 'false'))
    print(colors("Pamcary Tech Team - Gerenciamento de Hosts Cacti", "red", "true"))
    print(colors("\n    Remoção de hosts", "blue", "true"))
    print(
        colors("\n    O arquivo remove.txt deve estar neste diretório e conter apenas um hostname por linha.", "yellow",
               "false"))
    print(colors("\n    Digite o IP do host a ser removido, \"f\" para remover todos os hosts incluidos em remove.txt.",
                 "red", "false"))
    ip = input("    ")
    if ip == "f":
        file = open('remove.txt', 'r')
        for line in file:
            fields = line.split(';')
            ip = fields[0].rstrip()
            description = fields[1].rstrip()
            cmd = f"php {cli}remove_device.php --confirm --description={description}"
            print(cmd)
            print('\n')
            os.system(cmd)
    elif ip == "p":
        file = open('linux.txt', 'r')
        for line in file:
            fields = line.split(';')
            ip = fields[0].rstrip()
            description = fields[1].rstrip()
            if "gps-" in description:
                cmd = f"php {cli}remove_device.php --confirm --description={description}"
                print(
                    colors('\nRemovendo host ', 'red') +
                    colors(description, 'blue') +
                    colors(' IP: ', 'red') +
                    colors(ip, 'blue')
                )
                print(cmd)
                os.system(cmd)
            elif "pam-" in description:
                cmd = f"php {cli}remove_device.php --confirm --description={description} "
                print(
                    colors('\nRemovendo host ', 'red') +
                    colors(description, 'blue') +
                    colors(' IP: ', 'red') +
                    colors(ip, 'blue')
                )
                print(cmd)
                os.system(cmd)
    else:
        cmd = f"php {cli}remove_device.php --ip={ip} --confirm"
        print(cmd)
        os.system("  " + cmd)
