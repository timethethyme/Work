
#Script created by Kanon
#This script will replace all files in a folder with a zip of its contents excluding .py, .swp, and .zip


import os
from os import listdir
from os.path import isfile, join
import zipfile

class RarFiles():
    def __init__(self, path):
        self.files = []
        self.currdir = path
        self.GetFiles(path)
        self.CreateZips(path)
    def GetFiles(self, path):
        for f in os.listdir(path):
            self.files.append(f)
    def CreateZips(self, path):
        for f in self.files:
            if not f.endswith('.py'):
                if not f.endswith('.swp'):
                    if not f.endswith('.zip'):
                        print f
                        zipp = zipfile.ZipFile((path + '/' + f + '.zip'), 
                            mode='w')
                        zipp.write(path + '/' +  f)
                        zipp.close()
                        os.remove(path + '/' + f)
                        

#Example: 
#rar = RarFiles("/home/kanon/Desktop/rar")
