class GameOfLife():

    def __init__(self, state, wrapping):
        self.width = len(state[0])
        self.height = len(state)
        self.state = state
        self.wrapping = wrapping
        self.nextState = self.getNextState()

    def getNextState(self):
        nextState = [[False for i in range(self.width)] for j in range(self.height)]
        for r in range(self.height):
            for c in range(self.width):
                neighbors = self.getNeighbors(r, c)
                if self.state[r][c] and (neighbors == 3 or neighbors == 2):
                    nextState[r][c] = True
                elif not self.state[r][c] and neighbors == 3:
                    nextState[r][c] = True
        return nextState
    
    def getNeighbors(self, r, c):
        count = 0
        for i in range(-1,2):
            for j in range(-1,2):
                if self.wrapping:
                    if self.state[(r+i)%self.height][(c+j)%self.width] and not (i==0 and j==0):
                        count+=1
                else:
                    if 0<r+i<self.height and 0<c+j<self.width and self.state[r+i][c+j] and not (i==0 and j==0):
                        count+=1
        return count
    
    def updateState(self):
        self.state = self.nextState
        self.nextState = self.getNextState()

    def toString(self):
        result = ""
        for row in self.state:
            for elem in row:
                result+="1 " if elem else "0 "
            result+="\n"
        result+="\n"
        return result