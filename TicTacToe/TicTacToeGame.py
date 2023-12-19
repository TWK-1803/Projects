class TicTacToeGame:
    def __init__(self, filename):
        self.board = [["-" for c in range(3)] for r in range(3)]
        self.AITurn = 0
        self.turnNumber = 0
        self.moveDictionary = self.getMoveDictionary(filename)
        self.tokens = ["X", "O"]

    def start(self):
        self.resetBoard()
        self.AITurn = self.setAITurn()
        self.gameLoop()

    # getWinner returns the winning token if there is one
    def gameLoop(self):
        while self.getWinner() == "-" and not self.isDraw():
            print("\n" + self.toString(self.board))
            if self.isAITurn():
                move = self.getAIMove()
                print("The AI is playing " + str(move))
            else:
                move = self.getPlayerMove()
            self.playMove(move, self.tokens[self.turnNumber % 2])
        print("\n" + self.toString(self.board))
        if self.isDraw():
            print("DRAW! Nobody wins this game!")
        elif self.isAITurn():
            print("GAME OVER! The AI has won!")
        else:
            print("YOU WIN! Somehow you beat the AI!")
        self.playAgain()

    def playMove(self, move, token):
        i = move // 3
        j = move % 3
        self.board[i][j] = token
        if self.getWinner() == "-" and not self.isDraw():
            self.turnNumber += 1

    def playAgain(self):
        playAgain = input("(y/n) Play again? ")
        if playAgain.lower() == "y":
            self.start()
        elif playAgain.lower() == "n":
            print("Bye then!")
        else:
            print("Never mind, you can't be trusted with input. Bye!")

    def getWinner(self):
        if (
            self.board[0][0] != "-"
            and self.board[0][0] == self.board[1][0]
            and self.board[0][0] == self.board[2][0]
        ):
            return self.board[0][0]
        if (
            self.board[0][1] != "-"
            and self.board[0][1] == self.board[1][1]
            and self.board[0][1] == self.board[2][1]
        ):
            return self.board[0][1]
        if (
            self.board[0][2] != "-"
            and self.board[0][2] == self.board[1][2]
            and self.board[0][2] == self.board[2][2]
        ):
            return self.board[0][2]
        if (
            self.board[0][0] != "-"
            and self.board[0][0] == self.board[0][1]
            and self.board[0][0] == self.board[0][2]
        ):
            return self.board[0][0]
        if (
            self.board[1][0] != "-"
            and self.board[1][0] == self.board[1][1]
            and self.board[1][0] == self.board[1][2]
        ):
            return self.board[1][0]
        if (
            self.board[2][0] != "-"
            and self.board[2][0] == self.board[2][1]
            and self.board[2][0] == self.board[2][2]
        ):
            return self.board[0][0]
        if (
            self.board[0][0] != "-"
            and self.board[0][0] == self.board[1][1]
            and self.board[0][0] == self.board[2][2]
        ):
            return self.board[0][0]
        if (
            self.board[0][2] != "-"
            and self.board[0][2] == self.board[1][1]
            and self.board[0][2] == self.board[2][0]
        ):
            return self.board[0][2]
        return "-"

    def isDraw(self):
        return self.getValidMoves() == []

    def isAITurn(self):
        return self.turnNumber % 2 == self.AITurn

    def getAIMove(self):
        return self.moveDictionary[self.toString(self.board)]

    # player input is 1 indexed to ease playability, but it is 0 indexed internally
    def getPlayerMove(self):
        listOfValidMoves = self.getValidMoves()
        while True:
            move = input("Please input a valid move (" + str(listOfValidMoves) + ") ")
            if move.isnumeric():
                move = int(move)
                if move in listOfValidMoves:
                    return move - 1

    # 1 indexed list of moves so that it appears in the format of a phone numpad
    # 123
    # 456
    # 789
    def getValidMoves(self):
        listOfMoves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "-":
                    listOfMoves.append(i * 3 + j + 1)
        return listOfMoves

    def toString(self, board):
        output = ""
        for i in range(3):
            for j in range(3):
                output += board[i][j] + " "
            output += "\n"
        return output

    def resetBoard(self):
        self.board = [["-" for c in range(3)] for r in range(3)]
        self.turnNumber = 0

    def setAITurn(self):
        AITurn = input(
            "Would you like the AI to go 1st or 2nd? Input 1 or 2 then press Enter "
        )
        if AITurn == "1":
            return 0
        elif AITurn == "2":
            return 1
        else:
            print("You didn't enter a 1 or a 2. Defaulting to AI going first")
            return 0

    # dictionary entries are formatted as the example below. If not in the same location,
    # path to the move database must be supplied in filename
    # ---
    # ---
    # ---
    # 0
    # (only valid tokens are "X", "O", and "-")
    def getMoveDictionary(self, filename):
        file = open(filename, "r")
        lineNumber = 0
        tempArray = []
        moveDictionary = {}
        for line in file:
            lineNumber += 1
            line = line.rstrip()
            if lineNumber % 4 == 0:
                moveDictionary.update({self.toString(tempArray): int(line)})
                tempArray = []
                continue
            tempArray.append(list(line))
        file.close()
        return moveDictionary


if __name__ == "__main__":
    game = TicTacToeGame("TicTacToeMoveDictionary.txt")
    game.start()
