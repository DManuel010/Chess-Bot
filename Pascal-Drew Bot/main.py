import chess
from minimax import minimaxFunction
from alpha_beta import alpha_beta_search
from random_AI import randomAI
from alpha_beta import stockFish

def startGame():

    # clear_stack
    return chess.Board()

#A simple program to increase the depth when there are less moves and decrease the depth when there are more moves
def depthCalculator(numberOfMoves):
    if numberOfMoves<5:
        return 2
    if numberOfMoves<10:
        return 2
    if numberOfMoves>9 and numberOfMoves<15:
        return 2
    if numberOfMoves>14:
        return 1


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
    depth = 1
    while stillPlaying:
        turns += 1
        if turns % 2 > 0:
            print "white Turn:"
            currentPlayer = players[0]
            depth = depthCalculator(len(board.legal_moves))
            board.push(alpha_beta_search(board, "white",depth)) #New alpha beta, works, but sometimes crashes in error.
        else:
            print "black Turn"
            currentPlayer = players[1]
            board.push(randomAI(board))

        print board
        print "=================="

        if (board.is_stalemate() or board.is_insufficient_material()):
            print "DRAW"
            print "number of moves: " , turns
            stillPlaying = False

        elif board.is_game_over() and board.is_checkmate():

            print "Winner: " , currentPlayer
            print "number of moves: " , turns
            stillPlaying = False


main()
