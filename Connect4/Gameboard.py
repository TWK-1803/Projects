class Gameboard:
    def __init__(
        self,
        playerTokens: list,
        connectionWinLength: int,
        width: int,
        height: int,
        board: list,
    ):
        self.getValidBoard(connectionWinLength, width, height, board)
        self.playerTokens = self.getValidPlayerTokens(playerTokens)
        self.turnNumber = self.numTokens()

    def start(self):
        self.resetBoard()
        self.gameLoop()

    def gameLoop(self):
        player = "1"
        while not self.isWinner():
            print()
            print(self.toString())
            move = self.getPlayerMove()
            self.dropInColumn(move - 1)
            player = str((self.turnNumber % len(self.playerTokens)) + 1)
        print(self.toString())
        if self.isWinner():
            print(f"GAME OVER! Player {player} wins!")
        elif self.isDraw():
            print("DRAW! Nobody wins this game!")
        self.playAgain()

    def getPlayerMove(self):
        listOfValidMoves = self.getValidMoves()
        player = str(self.turnNumber % len(self.playerTokens) + 1)
        while True:
            move = input(
                f"Player {player} ({self.playerTokens[int(player)-1]}), please input a valid move ({listOfValidMoves}) "
            )
            if move.isnumeric():
                move = int(move)
                if move > self.width:
                    print(
                        "Please input a valid number (See the list of valid moves in the prompt)"
                    )
                    continue
            else:
                print(
                    "Please only input numbers (See the list of valid moves in the prompt)"
                )
                continue
            if move in listOfValidMoves:
                return move

    def playAgain(self):
        playAgain = input("(y/n) Play again? ")
        if playAgain.lower() == "y":
            self.start()
        elif playAgain.lower() == "n":
            print("Bye then!")
        else:
            print("Never mind, you can't be trusted with input. Bye!")

    def numTokens(self):
        count = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.hasToken(i, j):
                    count += 1
        return count

    def hasToken(self, r, c):
        return self.board[r][c] != "-"

    def resetBoard(self):
        self.board = [["-" for col in range(self.width)] for row in range(self.height)]
        self.turnNumber = 0

    def getValidPlayerTokens(self, playerTokens):
        if "-" in playerTokens:
            print(
                "\nCannot have '-' as a token, defaulting to a 1 player game with token 'X'\n"
            )
            return ["X"]
        elif playerTokens == []:
            print(
                "\nMust input a list of tokens, defaulting to a 1 player game with token 'X'\n"
            )
            return ["X"]
        else:
            for elem in playerTokens:
                if len(elem) != 1:
                    print(
                        "\nTokens must be single characters, defaulting to a 1 player game with token 'X'\n"
                    )
                    return ["X"]
        return playerTokens

    def getValidBoard(self, connectionWinLength, width, height, board):
        if (
            board != []
            and self.isValidBoard(board)
            and self.isPossibleBoard(connectionWinLength, board)
            and width == len(board[0])
            and height == len(board)
        ):
            self.board = board
            self.width = len(board[0])
            self.height = len(board)
            self.connectionWinLength = connectionWinLength
        else:
            print(
                "\nEither board was not valid, dimensions were incorrect, or the given board cannot be won.\n"
                + "Defaulting to a blank one with dimensions 1x1 specified and win length 0"
            )
            self.width = 1
            self.height = 1
            self.connectionWinLength = 0
            self.board = [["-" for c in range(self.width)] for r in range(self.height)]

    def getValidMoves(self):
        possibleMoves = [i for i in range(self.width)]
        invalidMoves = []
        for move in possibleMoves:
            if not self.isValidMove(move):
                invalidMoves.append(move)
        validMoves = [x + 1 for x in possibleMoves if x not in invalidMoves]
        return validMoves

    def isValidMove(self, column):
        if self.hasToken(0, column) or not isinstance(column, int):
            return False
        if column < 0 or column >= self.width:
            return False
        return True

    def isValidBoard(self, board):
        for i in range(len(board) - 1):
            for j in range(len(board[0])):
                if board[i][j] != "-" and board[i + 1][j] == "-":
                    return False
        return True

    def isPossibleBoard(self, connectionWinLength, board):
        if len(board) < connectionWinLength and len(board[0]) < connectionWinLength:
            return False
        return True

    def toString(self):
        output = ""
        for i in range(self.height):
            for j in range(self.width):
                output += self.board[i][j] + " "
            output += "\n"
        return output

    def dropInColumn(self, column):
        if self.hasToken(0, column):
            return
        for i in range(self.height):
            if i == self.height - 1:
                self.updateBoard(i, column)
                return
            elif self.hasToken(i + 1, column):
                self.updateBoard(i, column)
                return

    def updateBoard(self, r, c):
        self.board[r][c] = self.playerTokens[self.turnNumber % len(self.playerTokens)]
        if not self.isGameOver():
            self.turnNumber += 1

    def isGameOver(self):
        return self.isDraw() or self.isWinner()

    def isWinner(self):
        return (
            self.isHorizontalWin()
            or self.isVerticalWin()
            or self.isUpDiagonalWin()
            or self.isDownDiagonalWin()
        )

    def isDraw(self):
        return self.getValidMoves() == []

    def isHorizontalWin(self):
        for r in range(self.height):
            inARow = 0
            for c in range(self.width):
                if c == 0 and self.hasToken(r, c):
                    inARow = 1
                elif self.hasToken(r, c) and self.board[r][c - 1] != self.board[r][c]:
                    inARow = 1
                elif self.hasToken(r, c) and self.board[r][c - 1] == self.board[r][c]:
                    inARow += 1
                else:
                    inARow = 0
                if inARow == self.connectionWinLength:
                    return True
        return False

    def isVerticalWin(self):
        for c in range(self.width):
            inARow = 0
            for r in range(self.height):
                if r == 0 and self.hasToken(r, c):
                    inARow = 1
                elif self.hasToken(r, c) and self.board[r - 1][c] != self.board[r][c]:
                    inARow = 1
                elif self.hasToken(r, c) and self.board[r - 1][c] == self.board[r][c]:
                    inARow += 1
                else:
                    inARow = 0
                if inARow == self.connectionWinLength:
                    return True
        return False

    def isUpDiagonalWin(self):
        startrow = self.connectionWinLength - 1
        for i in range(startrow, self.height):
            r = i
            c = 0
            if self.isWinInThisUpDiagonal(r, c):
                return True

        endcolumn = self.connectionWinLength
        for i in range(1, endcolumn):
            r = self.height - 1
            c = i
            if self.isWinInThisUpDiagonal(r, c):
                return True
        return False

    def isWinInThisUpDiagonal(self, r, c):
        while not r < 0 and not c >= self.width:
            if (c == 0 or r == self.height - 1) and self.hasToken(r, c):
                inARow = 1
            elif self.hasToken(r, c) and self.board[r + 1][c - 1] != self.board[r][c]:
                inARow = 1
            elif self.hasToken(r, c) and self.board[r + 1][c - 1] == self.board[r][c]:
                inARow += 1
            else:
                inARow = 0
            if inARow == self.connectionWinLength:
                return True
            r -= 1
            c += 1
        return False

    def isDownDiagonalWin(self):
        startrow = self.height - self.connectionWinLength
        for i in range(startrow, 0, -1):
            r = i
            c = 0
            if self.isWinInThisDownDiagonal(r, c):
                return True

        endcolumn = self.connectionWinLength
        for i in range(endcolumn):
            r = 0
            c = i
            if self.isWinInThisDownDiagonal(r, c):
                return True
        return False

    def isWinInThisDownDiagonal(self, r, c):
        while not r >= self.height and not c >= self.width:
            if (c == 0 or r == 0) and self.hasToken(r, c):
                inARow = 1
            elif self.hasToken(r, c) and self.board[r - 1][c - 1] != self.board[r][c]:
                inARow = 1
            elif self.hasToken(r, c) and self.board[r - 1][c - 1] == self.board[r][c]:
                inARow += 1
            else:
                inARow = 0
            if inARow == self.connectionWinLength:
                return True
            r += 1
            c += 1
        return False
