import chess
from minimax import minimaxFunction
from alpha_beta import alpha_beta_search
from random_AI import randomAI


def startGame():

    # clear_stack
    return chess.Board()



def main():
    '''
    Simulates a game of chess by looping two AI players' actions
    '''

    turns = 0               # turn counter
    stillPlaying = True     # outer loop boolean
    player1 = "white"
    player2 = "black"

    players = [player1, player2]
    board = startGame()             # gets initial board state
    #print board

    while stillPlaying:

        turns += 1
        if turns % 2 > 0:
            currentPlayer = players[0]
            board.push(minimaxFunction(board,1,currentPlayer))
            #move = alpha_beta_search(board, currentPlayer,2) DO NOT DO ALPHA BETA IT DOES NOT WORK
        else:
            currentPlayer = players[1]
            board.push(randomAI(board))

        #print board
        #print "=================="

        if (board.is_stalemate() or board.is_insufficient_material()):
            return ("draw", turns)
            #print "DRAW"
            #print "number of moves: " , turns
            stillPlaying = False

        elif board.is_game_over() and board.is_checkmate():
            return (currentPlayer, turns)
            #print "Winner: " , currentPlayer
            #print "number of moves: " , turns
            stillPlaying = False

i = 0
games = []
totalMoves = 0
whiteCount = 0
blackCount = 0
drawCount = 0

while i < 15:
    currentGame = main()
    games.append(currentGame)
    totalMoves += currentGame[1]

    if currentGame[0] == "white":
        whiteCount += 1
    elif currentgame[0] == "black":
        blackCount += 1
    else:
        drawCount += 1

    i += 1

totalGames = whiteCount + blackCount + drawCount
averageMoves = totalMoves / totalGames
print games
print "white games won: " , whiteCount
print "black games won: " , blackCount
print "games with draw: " , drawCount
print "Average moves: " , averageMoves
