#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import argparse
import sys
from datetime import date

# Constantes
user_default = "itamar.portela"
port_default = 5398
dir_origin = "~/pamcary/pkg"
dir_output = "/tmp"
today = "{}.{}.{}".format(date.today().year, date.today().month, date.today().day )


def argparser():
    parser = argparse.ArgumentParser(description='Easier ssh and scp')
    parser.add_argument('server', help="Servidor para a conexao")
    parser.add_argument('--transfer', "-t", action='store_false', help="Ativa transferencia de arquivos")
    parser.add_argument('--date', "-dt", action='store_true', help="Inserir data no arquivo")
    parser.add_argument('--port', "-p",                  help="Porta a ser utilizada, padrão 5398")
    parser.add_argument('--directory', "-d", default=" ~/pamcary/pkg/", required=False, help="Diretorio de origem")
    parser.add_argument('--filename', "-f",              help="Nome do arquivo a ser transferido")
    parser.add_argument('--output', "-o", default="/tmp", help="Diretorio de destino do arquivo")
    parser.add_argument('--user', "-u", default=user_default, help="Usuario para o acesso")
    args = parser.parse_args()
    return args


def ssh(user, server, port=None):
    if port is None:
        cmd = "ssh {}@{}.pamcary-interno.com.br".format(user, server)
    else:
        cmd = "ssh -p {} {}@{}.pamcary-interno.com.br".format(port, user, server)

    return cmd


def main(arg):
    user = argparser().user
    server = argparser().server
    port = argparser().port
    if argparser().transfer:
        print("Transferindo")
    else:
        cmd = ssh(user, server, port)
        print("Data atual: {}".format(today))
        print("Servidor: {}".format(server))
        print("Porta: {}".format(port))
        print("Comando: {}".format(cmd))
    os.system(cmd)


if __name__ == '__main__':
    sys.exit(main(sys.argv))




