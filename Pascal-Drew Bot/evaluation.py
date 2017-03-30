import chess
import chess.uci
def middleOfBoard(x, y):

    coordinate = (x, y)
    if (coordinate == (3,3) or coordinate == (3,4) or
        coordinate == (4,3) or coordinate == (4,4)):
        return True

    return False



def evaluationFunction(board, whoMoved, player):
    '''
    Evaluation function used to evaluate node values for the minimax function.

    Evaluation value depends upon two factors:
        1) The difference in total value of the remaining white and black pieces.
        2) The difference in amount of middle squares controlled by each player.

    For instance, if White has more pieces that are of greater value than Black,
    and there are more White pieces in the middle squares than Black, then
    the evaluation score for that state will be higher.  The opposite is also true.
    '''

    piecesValuesWhite = {chess.Piece.from_symbol('P'):1, chess.Piece.from_symbol('R'):5,
                        chess.Piece.from_symbol('N'):3, chess.Piece.from_symbol('B'):3,
                        chess.Piece.from_symbol('Q'):10, chess.Piece.from_symbol('K'):20, 'None':0}

    piecesValuesBlack = {chess.Piece.from_symbol('p'):1, chess.Piece.from_symbol('r'):5,
                        chess.Piece.from_symbol('n'):3, chess.Piece.from_symbol('b'):3,
                        chess.Piece.from_symbol('q'):10, chess.Piece.from_symbol('k'):20, 'None':0}

    whiteSum = 0        # total of white piece values
    blackSum = 0        # total of black piece values

    middleWhite = 0     # total white pieces in middle four squares
    middleBlack = 0     # total black pieces in middle four squares

    #Goes through each square in the board matrix. If the piece is white, then it takes the piece's value and adds it to whiteSum. Same thing for black.
    for squareRank in range(8):
        for squareFile in range(8):
            square = board.piece_at(chess.square(squareRank,squareFile))

            if square in piecesValuesWhite:
                whiteSum += piecesValuesWhite[square]

                if middleOfBoard(squareRank, squareFile):
                    middleWhite += 1

            elif square in piecesValuesBlack:
                blackSum += piecesValuesBlack[square]

                if middleOfBoard(squareRank, squareFile):
                    middleBlack += 1

    value = (whiteSum - blackSum) + (middleWhite - middleBlack) # evaluation value



    #Returns score for terminal states
    if board.is_checkmate() and whoMoved==player:
        return 999
    elif board.is_checkmate() and whoMoved!=player:
        return -999

    return value
