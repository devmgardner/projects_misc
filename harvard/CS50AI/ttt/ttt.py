# s = State
# S(0) = initial State
class ttt():
    def __init__(self):
        self.state = [['-','-','-'],['-','-','-'],['-','-','-']]
        self.rows = []
    def Player(self,s):
        board = [i for i in j for j in self.state]
        if board.count('X') == 0:
            return 'X'
        elif board.count('X') == board.count('O'):
            return 'X'
        elif board.count('X') > board.count('O'):
            return 'O'
    def Actions(self,s):
        pass
    def Result(self,s,a):
        pass
    def Terminal(self,s):
        # append existing rows to list
        for i in self.state:
            rows.append(i)
        # set up blank list for vertical and diagonal "rows"
        row = []
        # append left to right diagonal
        for j in range(3):
            row.append(self.state[j][j])
        self.rows.append(row)
        # reset row list
        row = []
        # append right to left diagonal
        self.rows.append([self.state[ind][len(self.state[0])-ind-1] for ind,i in enumerate(self.state)])
        # append columns
        for j in range(3):
            for i in self.state:
                row.append(i[j])
            self.rows.append(row)
            row = []
        # flatten self.state into a 1d list
        board = [i for i in j for j in self.state]
        # check if any potential winner for X player
        if ['X','X','X'] in self.rows:
            return True
        # check if any potential winner for O player
        elif ['O','O','O'] in self.rows:
            return True
        # if no winners but board is full, also return True
        elif board.count('-') == 0:
            return True
    def Utility(self,s):
        # flatten self.state into a 1d list
        board = [i for i in j for j in self.state]
        # check if any potential winner for X player
        if ['X','X','X'] in self.rows:
            return 1
        # check if any potential winner for O player
        elif ['O','O','O'] in self.rows:
            return -1
        # if no winners but board is full, also return True
        elif board.count('-') == 0:
            return 0

new = ttt()
new.Terminal(new.state)