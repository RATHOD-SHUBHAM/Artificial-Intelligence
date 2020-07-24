#!/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Vassilis Athitsos
# Written to be Python 2.4 compatible for omega

from copy import copy
import random
from maxconnect4 import *
import sys

class maxConnect4Game:
    def __init__(self):
        self.gameBoard = [[0 for i in range(7)] for j in range(6)]
        self.currentTurn = 1
        self.player = None
        self.gameFile = None
        self.minMaxGameBord = None
        self.next = None
        self.player1Score = 0
        self.player2Score = 0
        self.pieceCount = 0
        self.depthLevel = 0
        self.GamePlayer1Score = 0
        self.GamePlayer2Score = 0
        self.max = 9999
        self.min = -9999
        random.seed()

    # Count the number of pieces already played
    def checkPieceCount(self):
        self.pieceCount = sum(1 for row in self.gameBoard for piece in row if piece)

    # Output current game status to console
    def printGameBoard(self):
        def printGameBoard(self):
            print
            ' -----------------'
            for i in range(6):
                print
                ' |',
                for j in range(7):
                    print('%d' % self.gameBoard[i][j]),
                print
                '| '
            print
            ' -----------------'

    # Output current game status to file
    def printGameBoardToFile(self, outFile):
        # try:
        gameFile = open(outFile, 'w')
        # except:
        #     sys.exit('Error opening output file.')
        for row in self.gameBoard:
            gameFile.write(''.join(str(col) for col in row) + '\r\n')
        gameFile.write('%s\r\n' % str(self.currentTurn))

    # Place the current player's piece in the requested column
    def playPiece(self, column):
        if column >= 0 and column < 7:
            if not self.gameBoard[0][column]:
                for i in range(5, -1, -1):
                    if not self.gameBoard[i][column]:
                        self.gameBoard[i][column] = self.currentTurn
                        self.pieceCount += 1
                        return 1
        else:
            return False


    def aiPlay(self):
        minMaxGameBord = self.gameBoard.copy()
        score, col = self.minMax(True, self.min, self.max, 0, None, minMaxGameBord, self.currentTurn)
        result = self.playPiece(col)
        print('\n\nmove %d: Player %d, column %d\n' % (self.pieceCount, self.currentTurn, col+1))
        self.currentTurn = self.changePlayerTurn(self.currentTurn)


    def changePlayerTurn(self, player):
        if player == 2:
            return 1
        elif player == 1:
            return 2


    def computerTurn(self, column, turn, minMaxGameBord):
        if column >= 0 and column < 7:
            if not minMaxGameBord[0][column]:
                for i in range(5, -1, -1):
                    if not minMaxGameBord[i][column]:
                        minMaxGameBord[i][column] = turn
                        return minMaxGameBord, i

        return False, False


    def minMax(self, minmaxPlayer, alpha, beta, depthLevel, column, minMaxGameBord, player):
        if depthLevel == self.depthLevel:
            self.GamePlayer1Score, self.GamePlayer2Score = self.countScore(minMaxGameBord)

            if self.currentTurn == 1:
                return (self.GamePlayer1Score - self.GamePlayer2Score), column
            elif self.currentTurn == 2:
                return (self.GamePlayer2Score - self.GamePlayer1Score), column


        if minmaxPlayer:
            least = self.min
            lowest = None

            for i in range(0,7):
                result, row = self.computerTurn(i, player, minMaxGameBord)
                if result:
                    minMaxGameBord = result.copy()
                    utility, col = self.minMax(False, alpha, beta, depthLevel+1, i, minMaxGameBord, self.changePlayerTurn(player))
                    minMaxGameBord[row][i] = 0
                    least = max(least, utility)
                    if max(least, utility) == utility or not col:
                        lowest = col
                    alpha = max(alpha, least)

                    if beta <= alpha:
                        break

            return least, lowest
        else:
            high = self.max
            highest = None
            for i in range(0,7):
                result, row = self.computerTurn(i, player, minMaxGameBord)
                if result:
                    minMaxGameBord = result.copy()
                    utility, col = self.minMax(True, alpha, beta, depthLevel+1, i, minMaxGameBord, self.changePlayerTurn(player))
                    minMaxGameBord[row][i] = 0
                    high = min(high, utility)
                    if min(high, utility) == utility or not highest:
                        highest = col
                    beta = min(beta, high)

                if beta <= alpha:
                    break

            return high, highest

    def computer(self):
        while (self.pieceCount < 42):
            if self.player == 'human-next':
                print('Player', self.currentTurn, 'turn\n\n')
                result = False

                while(not result):
                    self.next = int(input("Enter the column number [1-7] where you would like to play :"))-1
                    result = self.playPiece(self.next)
                    if not result:
                        print("Enter number ranging from 1 to 7")
                self.player = 'computer-next'

            elif self.player == 'computer-next':
                print("Computer's Turn\n\n")
                if self.depthLevel > 42 - self.pieceCount:
                    self.depthLevel = 42 - self.pieceCount
                minMaxGameBord = self.gameBoard.copy()
                utility,col = self.minMax(True, self.min, self.max, 0, None, minMaxGameBord, self.currentTurn)
                self.playPiece(col)

                self.player = 'human-next'
            self.currentTurn = self.changePlayerTurn(self.currentTurn)

            self.player1Score, self.player2Score = self.countScore(self.gameBoard)
            self.printGameBoard()
            self.printGameBoardToFile('computer.txt')
            print('Score: Player 1 = %d, Player 2 = %d\n' % (self.player1Score, self.player2Score))

        if self.player1Score > self.player2Score:
            print("Player 1 Wins")
        elif self.player1Score < self.player2Score:
            print("Player 2 Wins")
        else:
            print("Draw")


    def human(self):
        while (self.pieceCount < 42):
            print('Player', self.currentTurn, 'turn')
            result = False
            while(not result):
                self.next = int(input("Enter the column number [1-7] where you would like to play : "))-1
                result = self.playPiece(self.next)
                if not result:
                    print("Enter number ranging from 1 to 7")
            self.currentTurn = self.changePlayerTurn(self.currentTurn)
            # self.countScore()
            self.player1Score, self.player2Score = self.countScore(self.gameBoard)
            self.printGameBoard()
            self.printGameBoardToFile('human.txt')
            print('Score: Player 1 = %d, Player 2 = %d\n' % (self.player1Score, self.player2Score))
        if self.player1Score > self.player2Score:
            print("Player 1 wins")
        elif self.player1Score < self.player2Score:
            print("Player 2 Wins")
        else:
            print("Draw")


    # Calculate the number of 4-in-a-row each player has
    def countScore(self, gameBoard):
        player1Score = 0
        player2Score = 0

        # Check horizontally
        for row in gameBoard:
            # Check player 1
            if row[0:4] == [1]*4:
                player1Score += 1
            if row[1:5] == [1]*4:
                player1Score += 1
            if row[2:6] == [1]*4:
                player1Score += 1
            if row[3:7] == [1]*4:
                player1Score += 1
            # Check player 2
            if row[0:4] == [2]*4:
                player2Score += 1
            if row[1:5] == [2]*4:
                player2Score += 1
            if row[2:6] == [2]*4:
                player2Score += 1
            if row[3:7] == [2]*4:
                player2Score += 1

        # Check vertically
        for j in range(7):
            # Check player 1
            if (gameBoard[0][j] == 1 and gameBoard[1][j] == 1 and
                   gameBoard[2][j] == 1 and gameBoard[3][j] == 1):
                player1Score += 1
            if (gameBoard[1][j] == 1 and gameBoard[2][j] == 1 and
                   gameBoard[3][j] == 1 and gameBoard[4][j] == 1):
                player1Score += 1
            if (gameBoard[2][j] == 1 and gameBoard[3][j] == 1 and
                   gameBoard[4][j] == 1 and gameBoard[5][j] == 1):
                player1Score += 1
            # Check player 2
            if (gameBoard[0][j] == 2 and gameBoard[1][j] == 2 and
                   gameBoard[2][j] == 2 and gameBoard[3][j] == 2):
                player2Score += 1
            if (gameBoard[1][j] == 2 and gameBoard[2][j] == 2 and
                   gameBoard[3][j] == 2 and gameBoard[4][j] == 2):
                player2Score += 1
            if (gameBoard[2][j] == 2 and gameBoard[3][j] == 2 and
                   gameBoard[4][j] == 2 and gameBoard[5][j] == 2):
                player2Score += 1

        # Check diagonally

        # Check player 1
        if (gameBoard[2][0] == 1 and gameBoard[3][1] == 1 and
               gameBoard[4][2] == 1 and gameBoard[5][3] == 1):
            player1Score += 1
        if (gameBoard[1][0] == 1 and gameBoard[2][1] == 1 and
               gameBoard[3][2] == 1 and gameBoard[4][3] == 1):
            player1Score += 1
        if (gameBoard[2][1] == 1 and gameBoard[3][2] == 1 and
               gameBoard[4][3] == 1 and gameBoard[5][4] == 1):
            player1Score += 1
        if (gameBoard[0][0] == 1 and gameBoard[1][1] == 1 and
               gameBoard[2][2] == 1 and gameBoard[3][3] == 1):
            player1Score += 1
        if (gameBoard[1][1] == 1 and gameBoard[2][2] == 1 and
               gameBoard[3][3] == 1 and gameBoard[4][4] == 1):
            player1Score += 1
        if (gameBoard[2][2] == 1 and gameBoard[3][3] == 1 and
               gameBoard[4][4] == 1 and gameBoard[5][5] == 1):
            player1Score += 1
        if (gameBoard[0][1] == 1 and gameBoard[1][2] == 1 and
               gameBoard[2][3] == 1 and gameBoard[3][4] == 1):
            player1Score += 1
        if (gameBoard[1][2] == 1 and gameBoard[2][3] == 1 and
               gameBoard[3][4] == 1 and gameBoard[4][5] == 1):
            player1Score += 1
        if (gameBoard[2][3] == 1 and gameBoard[3][4] == 1 and
               gameBoard[4][5] == 1 and gameBoard[5][6] == 1):
            player1Score += 1
        if (gameBoard[0][2] == 1 and gameBoard[1][3] == 1 and
               gameBoard[2][4] == 1 and gameBoard[3][5] == 1):
            player1Score += 1
        if (gameBoard[1][3] == 1 and gameBoard[2][4] == 1 and
               gameBoard[3][5] == 1 and gameBoard[4][6] == 1):
            player1Score += 1
        if (gameBoard[0][3] == 1 and gameBoard[1][4] == 1 and
               gameBoard[2][5] == 1 and gameBoard[3][6] == 1):
            player1Score += 1

        if (gameBoard[0][3] == 1 and gameBoard[1][2] == 1 and
               gameBoard[2][1] == 1 and gameBoard[3][0] == 1):
            player1Score += 1
        if (gameBoard[0][4] == 1 and gameBoard[1][3] == 1 and
               gameBoard[2][2] == 1 and gameBoard[3][1] == 1):
            player1Score += 1
        if (gameBoard[1][3] == 1 and gameBoard[2][2] == 1 and
               gameBoard[3][1] == 1 and gameBoard[4][0] == 1):
            player1Score += 1
        if (gameBoard[0][5] == 1 and gameBoard[1][4] == 1 and
               gameBoard[2][3] == 1 and gameBoard[3][2] == 1):
            player1Score += 1
        if (gameBoard[1][4] == 1 and gameBoard[2][3] == 1 and
               gameBoard[3][2] == 1 and gameBoard[4][1] == 1):
            player1Score += 1
        if (gameBoard[2][3] == 1 and gameBoard[3][2] == 1 and
               gameBoard[4][1] == 1 and gameBoard[5][0] == 1):
            player1Score += 1
        if (gameBoard[0][6] == 1 and gameBoard[1][5] == 1 and
               gameBoard[2][4] == 1 and gameBoard[3][3] == 1):
            player1Score += 1
        if (gameBoard[1][5] == 1 and gameBoard[2][4] == 1 and
               gameBoard[3][3] == 1 and gameBoard[4][2] == 1):
            player1Score += 1
        if (gameBoard[2][4] == 1 and gameBoard[3][3] == 1 and
               gameBoard[4][2] == 1 and gameBoard[5][1] == 1):
            player1Score += 1
        if (gameBoard[1][6] == 1 and gameBoard[2][5] == 1 and
               gameBoard[3][4] == 1 and gameBoard[4][3] == 1):
            player1Score += 1
        if (gameBoard[2][5] == 1 and gameBoard[3][4] == 1 and
               gameBoard[4][3] == 1 and gameBoard[5][2] == 1):
            player1Score += 1
        if (gameBoard[2][6] == 1 and gameBoard[3][5] == 1 and
               gameBoard[4][4] == 1 and gameBoard[5][3] == 1):
            player1Score += 1

        # Check player 2
        if (gameBoard[2][0] == 2 and gameBoard[3][1] == 2 and
               gameBoard[4][2] == 2 and gameBoard[5][3] == 2):
            player2Score += 1
        if (gameBoard[1][0] == 2 and gameBoard[2][1] == 2 and
               gameBoard[3][2] == 2 and gameBoard[4][3] == 2):
            player2Score += 1
        if (gameBoard[2][1] == 2 and gameBoard[3][2] == 2 and
               gameBoard[4][3] == 2 and gameBoard[5][4] == 2):
            player2Score += 1
        if (gameBoard[0][0] == 2 and gameBoard[1][1] == 2 and
               gameBoard[2][2] == 2 and gameBoard[3][3] == 2):
            player2Score += 1
        if (gameBoard[1][1] == 2 and gameBoard[2][2] == 2 and
               gameBoard[3][3] == 2 and gameBoard[4][4] == 2):
            player2Score += 1
        if (gameBoard[2][2] == 2 and gameBoard[3][3] == 2 and
               gameBoard[4][4] == 2 and gameBoard[5][5] == 2):
            player2Score += 1
        if (gameBoard[0][1] == 2 and gameBoard[1][2] == 2 and
               gameBoard[2][3] == 2 and gameBoard[3][4] == 2):
            player2Score += 1
        if (gameBoard[1][2] == 2 and gameBoard[2][3] == 2 and
               gameBoard[3][4] == 2 and gameBoard[4][5] == 2):
            player2Score += 1
        if (gameBoard[2][3] == 2 and gameBoard[3][4] == 2 and
               gameBoard[4][5] == 2 and gameBoard[5][6] == 2):
            player2Score += 1
        if (gameBoard[0][2] == 2 and gameBoard[1][3] == 2 and
               gameBoard[2][4] == 2 and gameBoard[3][5] == 2):
            player2Score += 1
        if (gameBoard[1][3] == 2 and gameBoard[2][4] == 2 and
               gameBoard[3][5] == 2 and gameBoard[4][6] == 2):
            player2Score += 1
        if (gameBoard[0][3] == 2 and gameBoard[1][4] == 2 and
               gameBoard[2][5] == 2 and gameBoard[3][6] == 2):
            player2Score += 1

        if (gameBoard[0][3] == 2 and gameBoard[1][2] == 2 and
               gameBoard[2][1] == 2 and gameBoard[3][0] == 2):
            player2Score += 1
        if (gameBoard[0][4] == 2 and gameBoard[1][3] == 2 and
               gameBoard[2][2] == 2 and gameBoard[3][1] == 2):
            player2Score += 1
        if (gameBoard[1][3] == 2 and gameBoard[2][2] == 2 and
               gameBoard[3][1] == 2 and gameBoard[4][0] == 2):
            player2Score += 1
        if (gameBoard[0][5] == 2 and gameBoard[1][4] == 2 and
               gameBoard[2][3] == 2 and gameBoard[3][2] == 2):
            player2Score += 1
        if (gameBoard[1][4] == 2 and gameBoard[2][3] == 2 and
               gameBoard[3][2] == 2 and gameBoard[4][1] == 2):
            player2Score += 1
        if (gameBoard[2][3] == 2 and gameBoard[3][2] == 2 and
               gameBoard[4][1] == 2 and gameBoard[5][0] == 2):
            player2Score += 1
        if (gameBoard[0][6] == 2 and gameBoard[1][5] == 2 and
               gameBoard[2][4] == 2 and gameBoard[3][3] == 2):
            player2Score += 1
        if (gameBoard[1][5] == 2 and gameBoard[2][4] == 2 and
               gameBoard[3][3] == 2 and gameBoard[4][2] == 2):
            player2Score += 1
        if (gameBoard[2][4] == 2 and gameBoard[3][3] == 2 and
               gameBoard[4][2] == 2 and gameBoard[5][1] == 2):
            player2Score += 1
        if (gameBoard[1][6] == 2 and gameBoard[2][5] == 2 and
               gameBoard[3][4] == 2 and gameBoard[4][3] == 2):
            player2Score += 1
        if (gameBoard[2][5] == 2 and gameBoard[3][4] == 2 and
               gameBoard[4][3] == 2 and gameBoard[5][2] == 2):
            player2Score += 1
        if (gameBoard[2][6] == 2 and gameBoard[3][5] == 2 and
               gameBoard[4][4] == 2 and gameBoard[5][3] == 2):
            player2Score += 1

        return player1Score, player2Score