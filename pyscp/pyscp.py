#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
from os import path
import argparse
import sys
import simplejson as json
from datetime import date

def jsonr(json_name):
    item = ['user','domain', 'port', 'dir_origin', 'dir_destiny']
    f = open (json_name, "r")
    data = json.loads(f.read())
    f.close()
    return data
# Constantes
data = jsonr("default.json")

user_default = data['user']
domain_default = data['domain']
port_default = data['port']
dir_origin = data['dir_origin']
dir_output = data['dir_destiny']
today = ".{}.{}.{}".format(date.today().year, date.today().month, date.today().day )

def argparser():
    parser = argparse.ArgumentParser(description='Easier ssh and scp')
    parser.add_argument('server', help="Servidor para a conexao")
    parser.add_argument('--user', "-u", default=user_default, help="Usuario para o acesso")
    parser.add_argument('--port', "-p", help="Porta a ser utilizada, "u" para Default")
    parser.add_argument('--transfer', "-t", action='store_true', help="Ativa transferencia de arquivos")
    parser.add_argument('--dt', "-dt", action='store_true', help="Inserir data no arquivo")
    parser.add_argument('--directory', "-d", default=dir_origin, required=False,
                        help="Diretorio de origem")
    parser.add_argument('--filename', "-f",  default="all", nargs='*',
                        help="Nome do arquivo a ser transferido, padrão: all (todos)")
    parser.add_argument('--output', "-o", default=dir_output, help="Diretorio de destino do arquivo")

    args = parser.parse_args()
    return args


def ssh(user, server, port=None):
    if port is None:
        cmd = "ssh {}@{}.pamcary-interno.com.br".format(user, server)
    else:
        cmd = "ssh -p {} {}@{}.pamcary-interno.com.br".format(port, user, server)

    return cmd


def scp(user, server, dt, dir, filename, output, port):
    file = ""
    if filename == "all":
        filename = os.listdir(dir)
    for index, fileitem in enumerate(filename):
        # print (file)
        if path.exists("{}{}".format(dir, fileitem)):
            os.rename(dir + fileitem, dir + fileitem + today)
            file = file + fileitem + " "
        else:
            print("Arquivo não encontrado: {}\n".format(file))
    os.chdir(dir)
    if port is None:
        if dt:
            cmd = "scp {}{} {}@{}:{}".format(dir, file, user, server, output)
        else:
            cmd = "scp {}{} {}@{}:{}".format(dir, file, user, server, output)
    else:
        if dt:
            cmd = "scp -P{} {}{} {}@{}:{}".format(port, dir, file, user, server, output)
        else:
            cmd = "scp -P{} {}{} {}@{}:{}".format(port, dir, file, user, server, output)
    return cmd


def main(arg):

    user = argparser().user
    server = argparser().server
    port = argparser().port

    transfer = argparser().transfer
    dt = argparser().dt
    dir = argparser().directory
    filename = argparser().filename
    output = argparser().output

    if port == "u":
        port = "5398"

    cmd = scp(user, server, dt, dir, filename, output, port)

    if transfer:
        print("Transferindo\n")
        print("Data atual: {}".format(today))
        print("Servidor: {}".format(server))
        if port is not None:
            print("Porta: {}\n".format(port))
        print("Diretorio: {}".format(dir))
        print("Arquivos: ", end="")
        print(*filename, sep="")
        print("Destino: {}".format(output))
        print("Comando: {}\n".format(cmd))

    else:
        cmd = ssh(user, server, port)
        print("Data atual: {}\n".format(today))
        print("Servidor: {}".format(server))
        print("Porta: {}\n".format(port))
        print("Comando: {}\n".format(cmd))
    os.system(cmd)


if __name__ == '__main__':
    sys.exit(main(sys.argv))




