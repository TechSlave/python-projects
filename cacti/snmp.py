# -*- coding: utf-8 -*-
import os
import subprocess
import sys

#Classe de cores do Terminal
class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Função para inserir cor no texto
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

#Testando Root
euid = os.geteuid() 
if euid != 0:
  print(colors("Este script deve ser executado apenas pelo usuário ROOT! ",'red'))
  exit()
else:
    os.system("clear")
    print(colors("Usuário root identificado, prosseguindo...", 'green'))
    os.system('sleep 2')
    os.system('clear')


print(colors("                       ,*-.\n                       |  |\n                   ,.  |  |\n                   | |_|  | ,.\n                   `---.  |_| |\n                       |  .--`\n                       |  |\n                       |  | ", 'green', 'false'))
print(colors("                 Pamcary Tech Team\nInstalação e configuração do SNMP para uso do Cacti","blue","true"))
#Instalando o serviço
print(colors("\n=== Instalando pacote ",'red')+colors("snmpd ===",'blue'))
testPkg = os.path.exists("/etc/snmp")
if testPkg == True:
    print(colors("\nPacote já instalado, prosseguindo...",'green'))
    os.system("sleep 1")
else:
    print(colors("\nPacote não instalado, efetuando a instalação.",'blue'))
    os.system('yum install net-snmp -y')

testPkg = os.path.exists("/etc/snmp")
print(testPkg)
if testPkg == "false":
    print(colors("\nPacote não instalado corretamente.",'red'))
    exit()
else:
    #Gerando o arquivo de config, movendo para a pasta correta e definindo as permissões
    print(colors("\n=== Gerando arquivo de configuração - snmpd.conf ===\n",'blue'))

    os.system('cat /dev/null > snmpd.conf')
    os.system('echo \'com2sec     PamcaryCore     10.10.0.0/16    Pamcary\' >> snmpd.conf')
    os.system('echo \'com2sec     PamcaryLocal    localhost       Pamcary\' >> snmpd.conf')

    os.system('echo \'\ngroup       PamcaryGrp      v1              PamcaryCore\' >> snmpd.conf')
    os.system('echo \'group       PamcaryGrp      v2c             PamcaryCore\' >> snmpd.conf')
    os.system('echo \'group       PamcaryGrp      v1              PamcaryLocal\' >> snmpd.conf')
    os.system('echo \'group       PamcaryGrp      v2c             PamcaryLocal\' >> snmpd.conf')

    os.system('echo \'\nview        all             included        .1\' >> snmpd.conf')

    os.system('echo \'\naccess      PamcaryGrp  ""          any             noauth  exact   all     none    none\' >> snmpd.conf')
    os.system('sleep 1')
    os.system('cat snmpd.conf')
    print(colors("\n=== Arquivo Gerado, copiando para a pasta ",'blue')+colors("/etc/snmp/ ===",'yellow'))
    os.system("cp snmpd.conf /etc/snmp")
    print(colors("\n=== Ajustando permissões do arquivo ",'blue')+colors('snmpd.conf ===','blue'))
    os.system('chown root:root /etc/snmp/snmpd.conf;chmod 777 /etc/snmp/snmpd.conf')
    #Iniciando e ativando o serviço
    print(colors("\nIniciando serviço snmp",'blue'))
    os.system('service snmpd start')
    os.system('service snmpd restart')
    #Incluindo na inicialização
    print(colors("\n=== Incluindo o serviço snmp na inicialização do sistema ===",'blue'))
    testService = os.path.exists("/etc/systemd/system/multi-user.target.wants/snmpd.service")
    if testService == "false":
        os.system('chkconfig --add snmpd \\%s > /dev/null')
        os.system('systemctl enable --add snmpd')
        print(colors("\nServiço incluído com sucesso na inicialização.",'green','true'))
    else:
        print(colors("\nServiço já existente.",'green'))
    print 
    print(colors("\n  Instalação e configuração efetuada!",'green','true'))