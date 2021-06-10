#!/usr/bin/python3
# -*- coding: utf-8 -*-
import simplejson as json

# JSON file
item = ['user','domain', 'port', 'dir_origin', 'dir_destiny']

f = open ('default.json', "r")


data = json.loads(f.read())
print(data['user'])
# Iterating through the json
# list
#for i in data['default_data']:
#    print(i)

  
# Closing file
f.close()