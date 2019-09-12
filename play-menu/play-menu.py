# -*- coding: utf-8 -*-
import os


def listdirs(folder):
    return [
        d for d in (os.path.join(folder, d1) for d1 in os.listdir(folder))
        if os.path.isdir(d)
    ]


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


path = '/var/git/playbooks'
files = []
playbooks = listdirs(path)
ip = '0.0.0.0'
print(Bcolors.BOLD + Bcolors.FAIL + '########## - Pamcary Linux Team - ##########' + Bcolors.ENDC)
print(Bcolors.OKGREEN + '\n          Menu Playbooks\n' + Bcolors.ENDC)

d = dict()

counter = 0

for name in playbooks:
    if name in d:
        continue
    d[name] = counter
    counter += 1


d = {v: k for k, v in d.items()}
x = 0
for y in playbooks:
    print(Bcolors.FAIL + '({0}) '.format(x) + Bcolors.ENDC + '- {0}'.format(y.replace("/var/git/playbooks/", "")))
    x += 1

opt1 = input('\nSelect playbook: ')
os.system('clear')


def switch(argument):
    return d.get(argument, "Invalid option")


pb_dir = switch(int(opt1))
pb = pb_dir.replace("/var/git/playbooks/", "")
pb_full = '{0}/{1}.yml'.format(pb_dir, pb,)
os.system('clear')
print(Bcolors.WARNING + "\n          Playbook selected:", pb + Bcolors.ENDC)
ip = input('\nInsert IP Address: ')

cmd = "ansible-playbook -i '{0},' {1}".format(ip, pb_full)
os.system('clear')
decision = input(Bcolors.OKBLUE + '\nExecuting' + Bcolors.FAIL + f' {pb}' + Bcolors.OKBLUE + ' on ' + Bcolors.WARNING + f'{ip}' + Bcolors.OKBLUE + '. Continue? <y/n> ' + Bcolors.ENDC)
if decision == "y":
    os.system('clear')
    print(Bcolors.OKGREEN + "\n\n          Executing playbook", pb, "\n" + Bcolors.ENDC)
    os.system(cmd)
elif decision == "n":
    os.system('clear')
    print(Bcolors.FAIL + "\n\n          Execution terminated.\n\n" + Bcolors.ENDC)
