import chess
import random

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

def pascalTest():
    board = chess.Board()
    color = True #True=White Black=false
    num = 0 #Number of moves

    #Runs the chess game until win, draw, or stalemate hmmm
    while(True):
        board.push(randomAI(board))
        num=num+1
        print board
        print "=============================="
        if board.is_stalemate() or board.is_insufficient_material() or board.can_claim_threefold_repetition() or board.can_claim_fifty_moves() or board.can_claim_draw():
            print "Stalemate or Draw"
            print "Number of Moves: ",num
            break;
        if board.is_game_over() or board.is_checkmate():
            if color:
                print "White Won"
            else:
                print "Black Won"
            print "Number of Moves: ",num
            break;
        color=color

def drewTest():
    turns = 0       # turn counter
    stillPlaying = True     # outer loop boolean
    player_white = True     # white = true, black = false

    board = startGame()

    while stillPlaying:

        board.push(randomAI(board))
        turns += 1

        print board
        print "=================="

        if (board.is_stalemate() or board.is_insufficient_material() or
            board.can_claim_threefold_repetition() or board.can_claim_fifty_moves() or
            board.can_claim_draw()):

            print "DRAW"
            stillPlaying = False
            print "number of moves: " , turns

        elif board.is_game_over() and board.is_checkmate():

            if player_white:
                print "White Won"
            else:
                print "Black Won"

            print turns
            stillPlaying = False

        color != color

def main():
    drewTest()

main()
