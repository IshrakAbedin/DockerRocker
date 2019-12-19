#!/bin/false
import os

def convertPathToAbsolutePath(path):
    if(path[0] == '/'):
        return path
    elif(path[0] == '.' and path[1] == '/'):
        return os.getcwd() + str(path).lstrip('.')
    else:
        return os.getcwd() + '/' + path