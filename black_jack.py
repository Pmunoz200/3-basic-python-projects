import random

#Codes for the card icon
spades = u"\u2660"
clubes = u"\u2663"
diamond = u"\u2666"
hearth = u"\u2665"

class Cards:
    card = (2,3,4,5,6,7,8,9,10,'J','Q','K','A')
    pinta = (u"\u2660",u"\u2663",u"\u2666",u"\u2665")

    #Gives the first 2 random cards to de player
    def __init__(self):
        self.number = []
        self.suit = []
        for i in range(2):
            self.number.append(random.choice(self.card))
            self.suit.append(random.choice(self.pinta))
        self.imprimir_cartaP()

    #Prints the first 2 cards given to the player
    def imprimir_cartaP(self):
        for i in range(5):
            if i == 0:
                print(f'|{self.number[0]}      | |{self.number[1]}      |')
            if i%2 != 0:
                # Mantains the format regardless of the 2 digit number
                if self.number[0] == 10:
                    print('|        | |       |')
                elif self.number[1] == 10:
                    print('|       | |        |')
                else:
                    print('|       | |       |')
            if i == 2:
                if self.number[0] == 10:
                    print(f'|   {self.suit[0]}    | |   {self.suit[1]}   |')
                elif self.number[1] == 10:
                    print(f'|   {self.suit[0]}   | |   {self.suit[1]}    |')
                else:
                    print(f'|   {self.suit[0]}   | |   {self.suit[1]}   |')
            elif i == 4:
                print(f'|      {self.number[0]}| |      {self.number[1]}|')
        
        self.total_puntos()

    #Adds the total points for the first draw of cards of the player
    def total_puntos(self):
        self.acum = 0
        ace = True
        for i in self.number:
            if type(i) is str:
                # Corrects the special cards, includig the ace
                if i == 'A':
                    var1 = self.acum + 11
                    if var1 > 21:
                        self.acum += 1
                        ace = True
                    else:
                        self.acum += 1
                        ace = False
                else:
                    self.acum += 10
            else:
                self.acum += i
        if ace:    
            self.var1 = 0
            print('\n' + str(self.acum) + '\n')
        else:
            var1 = self.acum + 10
            self.var1 = var1
            print('\n' + str(self.acum))
            print('\n' + str(var1) + '\n')         
    
    #Adds a new card to the player's hand, printing it alongside
    def add_card(self):
        self.number.append(random.choice(self.card))
        self.suit.append(random.choice(self.pinta))
        num = len(self.number) -1 
        for i in range(5):
            if i == 0:
                print(f'|{self.number[num]}      |')
            if i%2 != 0:
                if self.number[num] == 10:
                    print('|        |')
                else:
                    print('|       |')
            if i == 2:
                if self.number[num] == 10:
                    print(f'|   {self.suit[num]}    |')
                else:
                    print(f'|   {self.suit[num]}   |')
            elif i == 4:
                print(f'|      {self.number[num]}|')
        #Calls to add the points
        self.add_puntos()
    
    #Adds points and shows them to the player
    def add_puntos(self):
        num = len(self.number) -1 
        ace = True
        if type(self.number[num]) is str:
            if self.number[num] == 'A':
                    var1 = self.acum + 11
                    if var1 > 21:
                        self.acum += 1
                        ace = True
                    else:
                        ace = False
                        self.acum += 1
            else:
                self.acum += 10
        else:
            self.acum += self.number[num]
        if ace:
            self.var1 = 0    
            print('\n' + str(self.acum) + '\n')
        else:
            var1 = self.acum + 10
            self.var1 = var1
            print('\n' + str(self.acum))
            print('\n' + str(var1) + '\n')

    #Generates a random dealeer score and plays whith the highest player score against the dealer
    def stand(self):

        dealer = random.randint(16,24)
        player = max(self.acum,self.var1)
        print (f'The dealer got {dealer}, \n')
        if dealer < 21:
            if dealer > player:
                print('You have lost to the dealer')
            else:
                print('Congratulations, you have won')
        else:
            print('Congratulations, you have won')

    #Checks if the player has gone over the 21 permited points to stop the game or not
    def game_state(self):
        if self.acum >21:
            print('You have lost, you went over 21')
            return False
        else:
            return True



crds = Cards()
active = True

#Mantains active the game until either the player goes over 21 or it plays against the dealer (Stand)
while active:
    command = input('What\'s your play?\n- Hit "A"\n- Stand "S"\n- Salir "E" ').lower()
    print('\n')
    if command == 'a':
        crds.add_card()
    elif command == 'e':
        active = False
    elif command == 's':
        crds.stand()
        active = False
    if active:
        active = crds.game_state()
