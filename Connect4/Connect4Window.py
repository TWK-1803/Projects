from setuptools import setup
from Gameboard import Gameboard
from Connect4AIAgent import Connect4AIAgent
import pygame
import time

class Connect4Window:

    def __init__(self):
        self.width = 7
        self.height = 6
        self.connectionWinLength = 4
        self.playerTokens = ["X", "O"]
        self.AITurnNumber = 1
        self.board = [["-" for col in range(self.width)] for row in range(self.height)]
        self.newboard = Gameboard(self.playerTokens, self.connectionWinLength, self.width, self.height, self.board)
        self.AIAgent = Connect4AIAgent(self.newboard, self.AITurnNumber)
        self.surface = self.setupCanvas()
        self.font = pygame.font.SysFont(None, 36)

    def restart(self):
        self.newboard.resetBoard()
        self.getResetCanvas()
        self.AITurnNumber = self.getAITurnNumber()
        self.gameLoop()

    def gameLoop(self):
        quickIsGameOver = False
        needToDrawGameOverMessage = True
        self.drawText(f"What move do you want to make? ({self.newboard.getValidMoves()})")
        while True:
            move = -1
            playAgain = "?"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        playAgain = "y"
                    elif event.key == pygame.K_n:
                        playAgain = "n"
                    elif not self.isAITurn():
                        move = self.getKeyInput(event.key)

            if not quickIsGameOver:
                if not self.newboard.isGameOver():
                    self.drawTokens()
                    if self.isAITurn():
                        self.drawText("Thinking...")
                        move = self.AIAgent.getMove()
                    if move != -1:
                        self.dropInColumn(move-1)
                        if not self.isAITurn():
                            self.drawText(f"AI is playing {move}")
                            time.sleep(1)
                            self.drawText(f"What move do you want to make? ({self.newboard.getValidMoves()})")
                else:
                    quickIsGameOver = True

            else:
                self.drawTokens()
                if needToDrawGameOverMessage:
                    if not self.newboard.isDraw():
                        if self.isAITurn():
                            self.drawText(f"GAME OVER! You lost!")
                        else:
                            self.drawText(f"GAME OVER! Player wins!")
                    else:
                        self.drawText("DRAW! Nobody wins this game!")
                    needToDrawGameOverMessage = False
                    time.sleep(2)
                    self.drawText("Play again? (y/n)")
                else:
                    if playAgain == "y" or playAgain == "n":
                        self.playAgain(playAgain)

    def playAgain(self, key):
        if key == "y":
            self.AITurnNumber = self.getAITurnNumber()
            self.restart()
        elif key == "n":
            quit()
        else:
            quit()
    
    def setupCanvas(self):
        pygame.init()
        surface = pygame.display.set_mode((800,700))
        BLUE = (1,80,183)
        GREY = (180,180,180)
        surface.fill(BLUE)
        for r in range(1, self.height + 1):
            for c in range(1, self.width + 1):
                pygame.draw.circle(surface, GREY, (c*100, r*100), 45, 0)
        pygame.display.update()
        return surface

    def getResetCanvas(self):
        BLUE = (1,80,183)
        GREY = (180,180,180)
        self.surface.fill(BLUE)
        for r in range(1, self.height + 1):
            for c in range(1, self.width + 1):
                pygame.draw.circle(self.surface, GREY, (c*100, r*100), 45, 0)
        columnNumbers = "1            2             3            4             5            6             7"
        img = self.font.render(columnNumbers, True, (0,0,0))
        self.surface.blit(img, (95, 650))
        pygame.display.update()

    def drawTokens(self):
        RED = (232,42,13)
        YELLOW = (240,206,0)
        GREY = (180,180,180)
        for r in range(1, self.height + 1):
            for c in range(1, self.width + 1):
                if self.newboard.board[r-1][c-1] == "-":
                    COLOR = GREY
                elif self.newboard.board[r-1][c-1] == "X":
                    COLOR = RED
                elif self.newboard.board[r-1][c-1] == "O":
                    COLOR = YELLOW
                pygame.draw.circle(self.surface, COLOR, (c*100, r*100), 45, 0)
        pygame.display.update()
    
    def drawText(self, text):
        img = self.font.render(text, True, (0,0,0))
        self.getResetCanvas()
        self.drawTokens()
        self.surface.blit(img, (50,10))
        pygame.display.update()

    def dropInColumn(self, column):
        if self.newboard.hasToken(0,column):
            return (0, 0)
        for i in range(self.newboard.height):
            if i == self.newboard.height-1:
                self.updateBoard(i, column)
                return
            elif self.newboard.hasToken(i+1, column):
                self.updateBoard(i, column)
                return

    def updateBoard(self,r,c):
        self.newboard.board[r][c] = self.playerTokens[self.newboard.turnNumber % len(self.playerTokens)]
        if not self.newboard.isGameOver():
            self.newboard.turnNumber += 1 

    def getAITurnNumber(self):
        AITurnNumber = -1
        self.getResetCanvas()
        self.drawText("Will the AI play 1st or 2nd? Press 1 or 2.")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                        AITurnNumber = 1
                    elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                        AITurnNumber = 2
            if AITurnNumber == 1 or AITurnNumber == 2:
                return AITurnNumber
    
    def getPlayerMove(self):
        listOfValidMoves = self.newboard.getValidMoves()
        player = str(self.newboard.turnNumber % len(self.newboard.playerTokens) + 1)
        while True:
            move = input(f"Player {player} ({self.newboard.playerTokens[int(player)-1]}), please input a valid move ({listOfValidMoves}) ")
            if move.isnumeric():
                move = int(move)
                if move > self.newboard.width:
                    print("Please input a valid number (See the list of valid moves in the prompt)")
                    continue
            else:
                print("Please only input numbers (See the list of valid moves in the prompt)")
                continue
            if move in listOfValidMoves:
                return move
    
    def getKeyInput(self, key):
        move = -1
        if key == pygame.K_1 or key == pygame.K_KP1:
            move = 1
        if key == pygame.K_2 or key == pygame.K_KP2:
            move = 2
        if key == pygame.K_3 or key == pygame.K_KP3:
            move = 3
        if key == pygame.K_4 or key == pygame.K_KP4:
            move = 4
        if key == pygame.K_5 or key == pygame.K_KP5:
            move = 5
        if key == pygame.K_6 or key == pygame.K_KP6:
            move = 6
        if key == pygame.K_7 or key == pygame.K_KP7:
            move = 7
        if move not in self.newboard.getValidMoves():
            move = -1
        return move
        
    def isAITurn(self):
        return self.AITurnNumber - 1 == self.newboard.turnNumber % len(self.newboard.playerTokens)

if __name__ == "__main__":
    newgame = Connect4Window()
    newgame.restart()
