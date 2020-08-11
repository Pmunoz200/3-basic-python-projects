import json
import getpass
import os

print ('\n')

class Authenticate:

    datos = {}
    
    # Creats an account with username and password
    def creat_acc(self):
        with open('data_base.json', 'r+') as json_file:
                data = json.load(json_file)
                self.username = input('Add username: ')
                cont = 0
                for i in data:
                    if i == self.username:
                        cont +=1
        if cont == 0:
            self.password = getpass.getpass('Password: ')
            self.datos.update({self.username: {'Password': self.password}})
            return True
        else:
            print('That user already excists')
            self.username= ''
            self.password = ''
    
    #Uploads the new username and password to the .json file

    def update(self):
        #Checks if the .json file is empty
        if os.path.getsize('/Users/pablomunoz/Documents/Programacion/5-Proyects_py/data_base.json') == 0:
            with open('data_base.json','w') as json_file:
                json.dump(self.datos,json_file, indent = 3)
        else:
            with open('data_base.json', 'r+') as json_file:
                data = json.load(json_file)
                data.update(self.datos)
                json_file.seek(0)
                json.dump(data,json_file,indent = 3)
    
    #Log-in checking if the user and password match in the .json file via iteration
    def log_in(self):
        with open('data_base.json', 'r+') as json_file:
                data = json.load(json_file)
                self.username = input('Username: ')
                for i in data:
                    if self.username == i:
                        self.password = getpass.getpass('Password: ')
                        if data[i]['Password'] == self.password:
                            return True

# A class to add the grades to the different users once ligged-in
class Notas:

    def __init__(self, username):
        self.state = True
        self.user = username
        #Def the first command once in grades
        self.command = input('What whould you like to do? \n - Add a class: "A" \n - Check your classes and grades "R"\n - Back to auth. menu "B"\n - Add grades "N"\n     ').lower()
        if self.command == 'b':
            self.state = False
    
    def add_class(self):
        clase = input('Input the class name: ')
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
                print('There are no classes created')
        self.add_State()

    def add_evaluations(self):
        print('Which class do you want to add the evaluation?\n')
        with open('data_base.json','r+') as json_file:
            data = json.load(json_file)
            for d in data[self.user]['Notas'].keys():
                print (d)
            clase = input('Input one of the classes shown: ')
            evla = input('Input the evaluation\'s name: ')
            porc = input('What is the percentage of the evaluation?: ')
            nota = input('Input the grade: ')
            conjun = [int(porc), int(nota)]
            data[self.user]['Notas'][clase].update({evla : conjun})
            json_file.seek(0)
            json.dump(data, json_file,indent=3)

        self.add_State()



    def add_State(self):
        self.command = input('What whould you like to do? \n - Add a class: "A" \n - Check your classes and grades "R"\n - Back to auth. menu "B"\n - Add grades "N"\n     ').lower()

    
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
    state = input('Auht. menu: \n "L" for log in \n "C" to create an account \n "E" exit program: ').lower()
    if state == 'l':
        value = user.log_in()
        if value:
            print('Welcome')
            ntas = Notas(user.username)
            check = True
            while check:
                ntas.commander()
                check = ntas.state
        else:
            print ('Wrong username or password')
    elif state == 'c':
        if user.creat_acc():
            user.update()
        
    elif state == 'e':
        active = False
    else:
        print('Input a valid command.')
