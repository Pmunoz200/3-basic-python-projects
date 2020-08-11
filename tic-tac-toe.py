import  random

class Game:
    lines= []
    def __init__(self):
        self.lines = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.print_gameboard()
    
    def print_gameboard(self):
        acom = 0
        for i in range(5):
            if i%2==0:
                print(f'{i-acom+1}  {self.lines[i-acom][0]}  |  {self.lines[i-acom][1]}  |  {self.lines[i-acom][2]}')
                acom += 1
            elif i%2!=0:
                print('  ---------------')
        print('   1    2     3')
        print('\n')
        return True

    def add_cross(self,row,column):
        self.lines[row-1][column-1] = 'x'
        self.print_gameboard()

    def computer(self):
        pos_position = [[0],[1],[2]]
        self.full_row = []
        for i in range(len(self.lines)):
            check = 3
            for j in range(3):
                if self.lines[i][j] == ' ':
                    check -= 1
                    pos_position[i].append(j)
            if check == 3:
                self.full_row.append(i)
        for i in reversed(self.full_row):
            pos_position.pop(i)
        
        if len(pos_position)>0:
            list1 = random.choice(pos_position)
            self.lines[list1[0]][list1[random.randrange(1,len(list1))]] = 'O'
            self.print_gameboard()
        else:
            print('The game has ended')
            return False

    def winning(self, piece):
        col1 = 0
        col2 = 0
        col3 = 0
        diag1 = 0
        diag2 = 0
        
        for i in range(3):
            conRow = 0
            for j in range(3):
                if self.lines[i][j] == piece:
                    conRow += 1
                if i == j:
                    if self.lines[i][j]== piece:
                        diag1 += 1
            if self.lines[i][0] == piece:
                col1 += 1
            elif self.lines[i][1] == piece:
                col2 += 1
            elif self.lines[i][2] == piece:
                col3 +=1
            if self.lines[i][2-i] == piece:
                diag2 += 1
                    
                        
            if conRow == 3 or col1 == 3 or col2 == 3 or col3 == 3 or diag1 == 3 or diag2 == 3:
                if piece == 'x':
                    print('The player WON')
                    break
                elif piece == 'O':
                    print('The computer WON')
                    break
        if conRow == 3 or col1 == 3 or col2 == 3 or col3 == 3 or diag1==3 or diag2 == 3:
            return False
        else:
            return True




game = Game()

active = True
while active:
    row = input('Select the row to place the "x": ')
    column = input('Select the column to place the "x": ')
    game.add_cross (int(row),int(column))
    active = game.winning('x')
    if active:
        game.computer()
        active = game.winning('O')
    if active:
        if len(game.full_row) == 3:
            active = False
        else:
            active = True

