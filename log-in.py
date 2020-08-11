import json
import getpass
import os

print ('\n')

class Authenticate:

    datos = {}
    
    # Crear una cuenta con user y password y guardarlo en el .json
    def creat_acc(self):
        with open('data_base.json', 'r+') as json_file:
                data = json.load(json_file)
                self.username = input('Ingrese un usuario: ')
                cont = 0
                for i in data:
                    if i == self.username:
                        cont +=1
        if cont == 0:
            self.password = getpass.getpass('Ingrese la contraseña: ')
            self.datos.update({self.username: {'Password': self.password}})
            return True
        else:
            print('That user already excists')
            self.username= ''
            self.password = ''
    
    #Subir los archivos creados con el creat_acc

    def update(self):
        #Revisar si el archivo esta vacio
        if os.path.getsize('/Users/pablomunoz/Documents/Programacion/5-Proyects_py/data_base.json') == 0:
            with open('data_base.json','w') as json_file:
                json.dump(self.datos,json_file, indent = 3)
        else:
            with open('data_base.json', 'r+') as json_file:
                data = json.load(json_file)
                data.update(self.datos)
                json_file.seek(0)
                json.dump(data,json_file,indent = 3)
    
    #Log-in revisando mediante iteración el archivo
    def log_in(self):
        with open('data_base.json', 'r+') as json_file:
                data = json.load(json_file)
                self.username = input('Ingrese su usuario: ')
                for i in data:
                    if self.username == i:
                        self.password = getpass.getpass('Ingrese la contraseña: ')
                        if data[i]['Password'] == self.password:
                            return True
                
class Notas:

    def __init__(self, username):
        self.state = True
        self.user = username
        #Definir la primera acción al entrar a notas
        self.command = input('Que desea hacer? \n - Añadir clase: "A" \n - Revisar tus clases y notas "R"\n - Volver al menú de autenticación "B"\n - Añadir notas "N"\n     ').lower()
        if self.command == 'b':
            self.state = False
    
    def add_class(self):
        clase = input('Ingrese el nombre de la asignatura: ')
        with open('data_base.json', 'r+') as json_file:
            data = json.load(json_file)
            cont = 0
            for i in data[self.user].keys():
                if i == 'Notas':
                    cont += 1
            if cont == 1:
                data[self.user]['Notas'].update({clase: {}})
            else:
                data[self.user].update({'Notas': {clase:{}}})
            json_file.seek(0)
            json.dump(data,json_file,indent=3)
        self.add_State()
    
    def check_file(self):
        with open('data_base.json', 'r+') as json_file:
            data = json.load(json_file)
            cont = 0
            for i in data[self.user].keys():
                if i == 'Notas':
                    cont += 1
            if cont == 1:
                print(data[self.user]['Notas'])
            else:
                print('No ha creado ningúna clase')
        self.add_State()

    def add_evaluations(self):
        print('A qué matería desea añadir las evaluaciones?\n')
        with open('data_base.json','r+') as json_file:
            data = json.load(json_file)
            for d in data[self.user]['Notas'].keys():
                print (d)
            clase = input('Ingrese el nombre de la clase que se muestra: ')
            evla = input('Ingrese el nombre de la evaluacion: ')
            porc = input('Ingrese el valor de la evaluación: ')
            nota = input('Igrese la nota sacada: ')
            conjun = [int(porc), int(nota)]
            data[self.user]['Notas'][clase].update({evla : conjun})
            json_file.seek(0)
            json.dump(data, json_file,indent=3)

        self.add_State()



    def add_State(self):
        self.command = input('Que desea hacer? \n - Añadir clase: "A" \n - Revisar tus clases y notas "R"\n - Volver al menú de autenticación "B"\n - Añadir notas "N"\n     ').lower()

    
    def commander(self):
        if self.command == 'a':
            self.add_class()
        elif self.command == 'b':
            self.state = False
        elif self.command == 'r':
            self.check_file()
        elif self.command == 'n':
            self.add_evaluations()

active = True
user = Authenticate()

while active:
    state = input('Ingrese: \n "L" para log in \n "C" para crear perfil \n "E" para salir: ').lower()
    if state == 'l':
        value = user.log_in()
        if value:
            print('Bienvenido')
            ntas = Notas(user.username)
            check = True
            while check:
                ntas.commander()
                check = ntas.state
        else:
            print ('Usuario o contraseña equivocada')
    elif state == 'c':
        if user.creat_acc():
            user.update()
        
    elif state == 'e':
        active = False
    else:
        print('ingrese un comando valido')
