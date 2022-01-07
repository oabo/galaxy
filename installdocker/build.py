#!/usr/bin/python3

import yaml
import os


def loadym(path):
    with open ( path,'r') as f:
        return yaml.load(f.read())

def ver_add_1(yml):
    ver = yml["version"]
    ver = ver.split('.')
    ver[2] = str(int(ver[2]) +1)
    version = ver[0] + '.' + ver[1] + '.'+ ver[2]
    yml['version'] = version
    print('new version is ',version)
    return yml

def write_yml(yml):
    with open(path,'w') as f:
        yaml.dump(yml,f)
        print(f)



if __name__ == "__main__":
    path = 'galaxy.yml'
    yml=loadym(path)
    yml=ver_add_1(yml)
    #print(yml)
    write_yml(yml)
    os.system('ansible-galaxy collection build --force')
