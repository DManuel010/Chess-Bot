import chess
import random


def randomAI(board):
    '''
    Selects one of the legal moves randomly and returns it
    '''

    moves = []
    for move in board.legal_moves:
        moves.append(move)

    move = random.choice(moves)
    legalMove = chess.Move.from_uci(str(move))
    while not legalMove in board.legal_moves:
        move = random.choice(moves)

    return legalMove
