# s = State
# S(0) = initial State
class ttt():
    def __init__(self):
        self.state = [['-','X','-'],['-','O','-'],['-','X','-']]
        self.rows = self.board = []
    def Player(self,s):
        self.board = [i for j in self.state for i in j]
        if self.board.count('X') == 0:
            return 'X'
        elif self.board.count('X') == self.board.count('O'):
            return 'X'
        elif self.board.count('X') > self.board.count('O'):
            return 'O'
    def Actions(self,s):
        player = self.Player(s)
        states = []
        for ind1,i in enumerate(self.state):
            for ind2,j in enumerate(i):
                if j == '-':
                    self.state[ind1][ind2] = player
                    states.append(self.state)
                    self.state[ind1][ind2] = '-'
        return states
    def Result(self,s,a):
        result = []
        for i in self.state:
            result.append(i)
        for ind1,i in enumerate(self.state):
            for ind2,j in enumerate(i):
                if j != '-':
                    result[ind1][ind2] = j
        return result
    def Terminal(self,s):
        # append existing rows to list
        for i in self.state:
            self.rows.append(i)
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
        # check if any potential winner for X player
        if ['X','X','X'] in self.rows:
            return True
        # check if any potential winner for O player
        elif ['O','O','O'] in self.rows:
            return True
        # if no winners but self.board is full, also return True
        elif self.board.count('-') == 0:
            return True
        else:
            return False
    def Utility(self,s):
        # flatten self.state into a 1d list
        self.board = [i for j in self.state for i in j]
        # check if any potential winner for X player
        if ['X','X','X'] in self.rows:
            return 1
        # check if any potential winner for O player
        elif ['O','O','O'] in self.rows:
            return -1
        # if no winners but self.board is full, also return True
        elif self.board.count('-') == 0:
            return 0
    def Max_Value(self,s):
        if self.Terminal(s):
            return self.Utility(s)
        v = float('-inf')
        for action in self.Actions(s):
            v = max(v, self.Min_Value(self.Result(s,action)))
        return v
    def Min_Value(self,s):
        if self.Terminal(s):
            return self.Utility(s)
        v = float('inf')
        for action in self.Actions(s):
            v = min(v, self.Max_Value(self.Result(s,action)))
        return v


new = ttt()
print(new.Terminal(new.state))
print(new.Result(new.state, [['O','-','-'],['-','-','-'],['-','-','-']]))