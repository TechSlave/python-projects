# -*- coding: utf-8 -*-
import os

# Functions definition


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def listdirs(folder):
    return [
        d for d in (os.path.join(folder, d1) for d1 in os.listdir(folder))
        if os.path.isdir(d)
    ]


def switch(argument):
    return d.get(argument, "Invalid option")


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


# -------------------------------------------
# Variables
path = '/var/git/playbooks'
files = []
playbooks = listdirs(path)
ip = '0.0.0.0'
d = dict()
counter = 0
x = 0
d = dict()
counter = 0
# -------------------------------------------

# Header
os.system('clear')
print(colors('######### - Pamcary Linux Team - #########', 'red', 'true'))
print(colors('\n         Menu Playbooks\n', 'green'))

# Searching playbooks and inserting them in a dictionary
for name in playbooks:
    if name in d:
        continue
    d[name] = counter
    counter += 1

# inverting value/key
d = {v: k for k, v in d.items()}

# Showing playbooks
for y in playbooks:
    # print(Bcolors.FAIL + '({0}) '.format(x) + Bcolors.ENDC + '- {0}'.format(y.replace("/var/git/playbooks/", "")))
    print(
        colors('({0})', 'red').format(x) +
        '- {0}'.format(y.replace("/var/git/playbooks/", ""))
          )
    x += 1
# Obtaining selection
opt1 = input(colors('\nSelect playbook: ', 'yellow'))
os.system('clear')
# Formatting playbooks variables
pb_dir = switch(int(opt1))
pb = pb_dir.replace("/var/git/playbooks/", "")
pb_full = '{0}/{1}.yml'.format(pb_dir, pb,)
os.system('clear')
# print(Bcolors.WARNING + "\n          Playbook selected:", pb + Bcolors.ENDC)
print(colors("\n          Playbook selected: ", 'red') +
      colors(pb, 'yellow')
      )
ip = input('\nInsert IP Address: ')
# Creating Ansible command
cmd = "ansible-playbook -i '{0},' {1}".format(ip, pb_full)
os.system('clear')
# decision = input(Bcolors.OKBLUE + '\nExecuting' + Bcolors.FAIL + f' {pb}' + Bcolors.OKBLUE + ' on ' + Bcolors.WARNING + f'{ip}' + Bcolors.OKBLUE + '. Continue? <y/n> ' + Bcolors.ENDC)
decision = input(
    colors('\nExecuting ', 'blue') +
    colors(pb, 'red') +
    colors(' on ', 'blue') +
    colors(ip, 'yellow') +
    colors('. Continue? <y/n> ', 'blue')
)

# Confirming action
if decision == "y":
    os.system('clear')
    print(colors("\n\n          Executing playbook: ", 'green') +
          colors(pb, 'green') +
          '\n'
          )
    os.system(cmd)
elif decision == "n":
    os.system('clear')
    print (colors("\n\n          Execution terminated.\n\n", 'red'))
