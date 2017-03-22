import chess
import random
from minimax import pascalMinimax


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

    while stillPlaying:

        turns += 1
        if turns % 2 > 0:
            currentPlayer = players[0]
            board.push(pascalMinimax(board, 1, currentPlayer))
        else:
            currentPlayer = players[1]
            board.push(randomAI(board))

        # board.push(randomAI(board))   # random move
        # board.push(pascalMinimax(board, 2))    # minimax

        print board
        print "=================="

        if (board.is_stalemate() or board.is_insufficient_material() or
            board.can_claim_threefold_repetition() or board.can_claim_fifty_moves() or
            board.can_claim_draw()):

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
