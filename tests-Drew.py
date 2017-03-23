import chess
import random
from minimax import pascalMinimax
from minimax import alpha_beta_search

def startGame():
    # clear_stack
    return chess.Board()



def randomAI(board): #Selects one of the legal moves randomly and returns it
    moves = []
    for move in board.legal_moves:
        moves.append(move)
    move = random.choice(moves)
    while not chess.Move.from_uci(str(move)) in board.legal_moves:
        move = random.choice(moves)

    return chess.Move.from_uci(str(move))



def drewTest():
    turns = 0               # turn counter
    stillPlaying = True     # outer loop boolean
    player1 = "white"
    player2 = "black"
    players = [player1, player2]
    board = startGame()
    print board
    while stillPlaying:
        turns += 1
        if turns % 2 > 0:
            currentPlayer = players[0]
            board.push(pascalMinimax(board,1,currentPlayer))
            #move = alpha_beta_search(board, currentPlayer,2) DO NOT DO ALPHA BETA IT DOES NOT WORK
            #board.push(move)
        else:
            currentPlayer = players[1]
            board.push(stockfishAI(board))


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

def main():

    drewTest()

main()
