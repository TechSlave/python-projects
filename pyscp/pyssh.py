#!/usr/bin/python3
import sys
import os
param = sys.argv[1:]
user = "itamar.portela"
portu = 5398
if len(param) == 1:
    server = param[0]
    print("Servidor: {}".format(server))
    cmd = "ssh {}@{}.pamcary-interno.com.br".format(user, server)
    os.system(cmd)
elif len(param) == 2:
    if param[1] == "u":
        server = param[0]
        port = portu
        print("Servidor: {}".format(server))
        print("Porta: {}".format(port))
        cmd = "ssh -p {} {}@{}.pamcary-interno.com.br".format(port, user, server)
        print("Comando: {}".format(cmd))
        os.system(cmd)
    else:
        server = param[0]
        port = param[1]
        print("Servidor: {}".format(server))
        print("Port: {}".format(port))
        cmd = "ssh -p {} {}@{}.pamcary-interno.com.br".format(port, user, server)
        print("Comando: {}".format(cmd))
        os.system(cmd)
else:
    print("Digitar ao menos o servidor")






