import chess
from minimax import pascalMinimax
from alpha_beta import alpha_beta_search
from random_AI import randomAI
import random


def startGame():

    # clear_stack
    return chess.Board()



def main():
    '''
    Simulates a game of chess by looping two AI players' actions
    '''
    drewTest()
def randomAI(board): #Selects one of the legal moves randomly and returns it
    moves = []
    for move in board.legal_moves:
        moves.append(move)
    move = random.choice(moves)
    while not chess.Move.from_uci(str(move)) in board.legal_moves:
        move = random.choice(moves)

    return chess.Move.from_uci(str(move))

def stockfishAI(board):
    import chess.uci
    engine = chess.uci.popen_engine("stockfish")
    engine.uci()
    print engine.name
    engine.position(board)
    bestmove, ponder = engine.go(movetime=2000)
    return chess.Move.from_uci(str(bestmove))

def drewTest():
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
            board.push(pascalMinimax(board,2,currentPlayer))
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
