from Gameboard import Gameboard
import copy
import random
import time


class Connect4AIAgent:
    def __init__(self, Gameboard, AITurnNumber):
        self.gameboard = Gameboard
        self.AITurnNumber = AITurnNumber - 1
        self.width = 7
        self.height = 6
        self.connectionWinLength = 4
        self.AIIsMaximizing = True
        self.fillValue = 9999
        self.depth = 5

    def getMove(self):
        if self.isBlank(self.gameboard.board):
            return 4
        start = time.time()
        moveEvalutations = [self.fillValue for i in range(self.width)]
        validMoves = self.getValidMoves(self.gameboard.board)
        for move in validMoves:
            newboard = copy.deepcopy(self.gameboard.board)
            newboard = self.getBoardWithMove(newboard, self.gameboard.turnNumber, move)
            moveEvalutations[move] = self.alphaBeta(
                newboard, self.gameboard.turnNumber, self.depth, self.AIIsMaximizing
            )
        # print(moveEvalutations)
        minIndexes = self.getMinIndexes(moveEvalutations)
        end = time.time()
        self.adjustDepth(end - start)
        return random.choice(minIndexes) + 1

    def alphaBeta(
        self, board, turnNumber, depth, isMaximizingPlayer, alpha=-9999, beta=9999
    ):
        if depth == 0 or self.gameIsOver(board):
            return self.evaluateBoard(board, isMaximizingPlayer, depth)
        else:
            if isMaximizingPlayer:
                maxEvaluation = -9999
                for move in self.getValidMoves(board):
                    newboard = copy.deepcopy(board)
                    newboard = self.getBoardWithMove(newboard, turnNumber + 1, move)
                    evaluation = self.alphaBeta(
                        newboard,
                        turnNumber + 1,
                        depth - 1,
                        not isMaximizingPlayer,
                        alpha,
                        beta,
                    )
                    maxEvaluation = max(maxEvaluation, evaluation)
                    alpha = max(alpha, maxEvaluation)
                    if beta <= alpha:
                        break
                return maxEvaluation
            else:
                minEvaluation = 9999
                for move in self.getValidMoves(board):
                    newboard = copy.deepcopy(board)
                    newboard = self.getBoardWithMove(newboard, turnNumber + 1, move)
                    evaluation = self.alphaBeta(
                        newboard,
                        turnNumber + 1,
                        depth - 1,
                        not isMaximizingPlayer,
                        alpha,
                        beta,
                    )
                    minEvaluation = min(minEvaluation, evaluation)
                    beta = min(beta, minEvaluation)
                    if beta <= alpha:
                        break
                return minEvaluation

    def evaluateBoard(self, board, isMaximizingPlayer, depth):
        if self.isWinner(board):
            if isMaximizingPlayer:
                return -100 - depth
            else:
                return 100 + depth
        else:
            horizontalScores = self.horizontalScores(board)
            verticalScores = self.verticalScores(board)
            upDiagonalScores = self.upDiagonalScores(board)
            downDiagonalScores = self.downDiagonalScores(board)
            player1Total = (
                horizontalScores[0]
                + verticalScores[0]
                + upDiagonalScores[0]
                + downDiagonalScores[0]
            )
            player2Total = (
                horizontalScores[1]
                + verticalScores[1]
                + upDiagonalScores[1]
                + downDiagonalScores[1]
            )
            totals = [player1Total, player2Total]
            if isMaximizingPlayer:
                return totals[(self.AITurnNumber + 1) % 2] - totals[self.AITurnNumber]
            else:
                return totals[self.AITurnNumber] - totals[(self.AITurnNumber + 1) % 2]

    def getTotalScores(self, player1Scores, player2Scores):
        player1Total = 0
        player2Total = 0
        for elem in player1Scores:
            if elem == 0:
                continue
            elif elem == 1:
                player1Total += 0.1
            elif elem == 2:
                player1Total += 0.3
            else:
                player1Total += 0.9
        for elem in player2Scores:
            if elem == 0:
                continue
            elif elem == 1:
                player2Total += 0.1
            elif elem == 2:
                player2Total += 0.3
            else:
                player2Total += 0.9
        return [player1Total, player2Total]

    def horizontalScores(self, board):
        player1Scores = []
        player2Scores = []
        player1Total = 0
        player2Total = 0
        for r in range(self.height):
            inARow = 0
            for c in range(self.width):
                if c == 0 and self.hasToken(board, r, c):
                    inARow = 1
                elif self.hasToken(board, r, c) and board[r][c - 1] != board[r][c]:
                    if board[r][c - 1] == "X":
                        player1Scores.append(inARow)
                    else:
                        player2Scores.append(inARow)
                    inARow = 1
                elif self.hasToken(board, r, c) and board[r][c - 1] == board[r][c]:
                    inARow += 1
                else:
                    if board[r][c - 1] == "X":
                        player1Scores.append(inARow)
                    else:
                        player2Scores.append(inARow)
                    inARow = 0
            scores = self.getTotalScores(player1Scores, player2Scores)
            player1Total += scores[0]
            player2Total += scores[1]
            player1Scores = []
            player2Scores = []
        return [player1Total, player2Total]

    def verticalScores(self, board):
        player1Scores = []
        player2Scores = []
        player1Total = 0
        player2Total = 0
        for c in range(self.width):
            inARow = 0
            for r in range(self.height):
                if r == 0 and self.hasToken(board, r, c):
                    inARow = 1
                elif self.hasToken(board, r, c) and board[r - 1][c] != board[r][c]:
                    if board[r - 1][c] == "X":
                        player1Scores.append(inARow)
                    else:
                        player2Scores.append(inARow)
                    inARow = 1
                elif self.hasToken(board, r, c) and board[r - 1][c] == board[r][c]:
                    inARow += 1
                else:
                    if board[r - 1][c] == "X":
                        player1Scores.append(inARow)
                    else:
                        player2Scores.append(inARow)
                    inARow = 0
            scores = self.getTotalScores(player1Scores, player2Scores)
            player1Total += scores[0]
            player2Total += scores[1]
            player1Scores = []
            player2Scores = []
        return [player1Total, player2Total]

    def upDiagonalScores(self, board):
        player1Total = 0
        player2Total = 0
        startrow = self.connectionWinLength - 1
        for i in range(startrow, self.height):
            r = i
            c = 0
            scores = self.scoresInThisUpDiagonal(board, r, c)
            player1Total += scores[0]
            player2Total += scores[1]

        endcolumn = self.connectionWinLength
        for i in range(1, endcolumn):
            r = self.height - 1
            c = i
            scores = self.scoresInThisUpDiagonal(board, r, c)
            player1Total += scores[0]
            player2Total += scores[1]
        return [player1Total, player2Total]

    def scoresInThisUpDiagonal(self, board, r, c):
        player1Scores = []
        player2Scores = []
        inARow = 0
        while not r < 0 and not c >= self.width:
            if c == 0 or r == self.height - 1:
                if self.hasToken(board, r, c):
                    inARow = 1
            elif self.hasToken(board, r, c) and board[r + 1][c - 1] != board[r][c]:
                if board[r + 1][c - 1] == "X":
                    player1Scores.append(inARow)
                else:
                    player2Scores.append(inARow)
                inARow = 1
            elif self.hasToken(board, r, c) and board[r + 1][c - 1] == board[r][c]:
                inARow += 1
            else:
                if board[r + 1][c - 1] == "X":
                    player1Scores.append(inARow)
                else:
                    player2Scores.append(inARow)
                inARow = 0
            r -= 1
            c += 1
        return self.getTotalScores(player1Scores, player2Scores)

    def downDiagonalScores(self, board):
        player1Total = 0
        player2Total = 0
        startrow = self.height - self.connectionWinLength
        for i in range(startrow, 0, -1):
            r = i
            c = 0
            scores = self.scoresInThisUpDiagonal(board, r, c)
            player1Total += scores[0]
            player2Total += scores[1]

        endcolumn = self.connectionWinLength
        for i in range(endcolumn):
            r = 0
            c = i
            scores = self.scoresInThisUpDiagonal(board, r, c)
            player1Total += scores[0]
            player2Total += scores[1]
        return [player1Total, player2Total]

    def scoresInThisDownDiagonal(self, board, r, c):
        player1Scores = []
        player2Scores = []
        while not r >= self.height and not c >= self.width:
            if (c == 0 or r == 0) and self.hasToken(board, r, c):
                inARow = 1
            elif self.hasToken(board, r, c) and board[r - 1][c - 1] != board[r][c]:
                if board[r - 1][c - 1] == "X":
                    player1Scores.append(inARow)
                else:
                    player2Scores.append(inARow)
                inARow = 1
            elif self.hasToken(board, r, c) and board[r - 1][c - 1] == board[r][c]:
                inARow += 1
            else:
                if board[r - 1][c - 1] == "X":
                    player1Scores.append(inARow)
                else:
                    player2Scores.append(inARow)
                inARow = 0
            r += 1
            c += 1
        return self.getTotalScores(player1Scores, player2Scores)

    def getMinIndexes(self, list):
        minIndexes = []
        minValue = min(list)
        for i in range(len(list)):
            if list[i] == minValue:
                minIndexes.append(i)
        return minIndexes

    def adjustDepth(self, timeForLastIteration):
        if timeForLastIteration < 5 and self.gameboard.turnNumber >= 10:
            self.depth += 1

    def getValidMoves(self, board):
        possibleMoves = [i for i in range(len(board[0]))]
        invalidMoves = []
        for move in possibleMoves:
            if not self.isValidMove(board, move):
                invalidMoves.append(move)
        validMoves = [x for x in possibleMoves if x not in invalidMoves]
        return validMoves

    def isValidMove(self, board, column):
        if self.hasToken(board, 0, column):
            return False
        if column < 0 or column >= len(board[0]):
            return False
        return True

    def getBoardWithMove(self, board, turnNumber, move):
        for i in range(len(board)):
            if i == len(board) - 1:
                return self.updateBoard(board, turnNumber, i, move)
            elif self.hasToken(board, i + 1, move):
                return self.updateBoard(board, turnNumber, i, move)

    def updateBoard(self, board, turnNumber, r, c):
        board[r][c] = self.gameboard.playerTokens[
            turnNumber % len(self.gameboard.playerTokens)
        ]
        return board

    def hasToken(self, board, r, c):
        return board[r][c] != "-"

    def gameIsOver(self, board):
        return self.isWinner(board) or self.isDraw(board)

    def isWinner(self, board):
        return (
            self.isHorizontalWin(board)
            or self.isVerticalWin(board)
            or self.isUpDiagonalWin(board)
            or self.isDownDiagonalWin(board)
        )

    def isDraw(self, board):
        return self.getValidMoves(board) == []

    def isBlank(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != "-":
                    return False
        return True

    def isHorizontalWin(self, board):
        for r in range(self.height):
            inARow = 0
            for c in range(self.width):
                if c == 0 and self.hasToken(board, r, c):
                    inARow = 1
                elif self.hasToken(board, r, c) and board[r][c - 1] != board[r][c]:
                    inARow = 1
                elif self.hasToken(board, r, c) and board[r][c - 1] == board[r][c]:
                    inARow += 1
                else:
                    inARow = 0
                if inARow == self.connectionWinLength:
                    return True
        return False

    def isVerticalWin(self, board):
        for c in range(self.width):
            inARow = 0
            for r in range(self.height):
                if r == 0 and self.hasToken(board, r, c):
                    inARow = 1
                elif self.hasToken(board, r, c) and board[r - 1][c] != board[r][c]:
                    inARow = 1
                elif self.hasToken(board, r, c) and board[r - 1][c] == board[r][c]:
                    inARow += 1
                else:
                    inARow = 0
                if inARow == self.connectionWinLength:
                    return True
        return False

    def isUpDiagonalWin(self, board):
        startrow = self.connectionWinLength - 1
        for i in range(startrow, self.height):
            r = i
            c = 0
            if self.isWinInThisUpDiagonal(board, r, c):
                return True

        endcolumn = self.connectionWinLength
        for i in range(1, endcolumn):
            r = self.height - 1
            c = i
            if self.isWinInThisUpDiagonal(board, r, c):
                return True
        return False

    def isWinInThisUpDiagonal(self, board, r, c):
        while not r < 0 and not c >= self.width:
            if (c == 0 or r == self.height - 1) and self.hasToken(board, r, c):
                inARow = 1
            elif self.hasToken(board, r, c) and board[r + 1][c - 1] != board[r][c]:
                inARow = 1
            elif self.hasToken(board, r, c) and board[r + 1][c - 1] == board[r][c]:
                inARow += 1
            else:
                inARow = 0
            if inARow == self.connectionWinLength:
                return True
            r -= 1
            c += 1
        return False

    def isDownDiagonalWin(self, board):
        startrow = self.height - self.connectionWinLength
        for i in range(startrow, 0, -1):
            r = i
            c = 0
            if self.isWinInThisDownDiagonal(board, r, c):
                return True

        endcolumn = self.connectionWinLength
        for i in range(endcolumn):
            r = 0
            c = i
            if self.isWinInThisDownDiagonal(board, r, c):
                return True
        return False

    def isWinInThisDownDiagonal(self, board, r, c):
        while not r >= self.height and not c >= self.width:
            if (c == 0 or r == 0) and self.hasToken(board, r, c):
                inARow = 1
            elif self.hasToken(board, r, c) and board[r - 1][c - 1] != board[r][c]:
                inARow = 1
            elif self.hasToken(board, r, c) and board[r - 1][c - 1] == board[r][c]:
                inARow += 1
            else:
                inARow = 0
            if inARow == self.connectionWinLength:
                return True
            r += 1
            c += 1
        return False
