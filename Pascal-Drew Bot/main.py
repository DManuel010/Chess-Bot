import chess
from minimax import pascalMinimax
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
    print board

    while stillPlaying:

        turns += 1
        if turns % 2 > 0:
            currentPlayer = players[0]
            board.push(pascalMinimax(board,1,currentPlayer))
            #move = alpha_beta_search(board, currentPlayer,2) DO NOT DO ALPHA BETA IT DOES NOT WORK
        else:
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
