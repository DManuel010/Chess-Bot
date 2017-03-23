import chess


def pascalHueristic(board):
    piecesValuesWhite = {chess.Piece.from_symbol('P'):1,chess.Piece.from_symbol('R'):5,chess.Piece.from_symbol('N'):3,chess.Piece.from_symbol('B'):3,chess.Piece.from_symbol('Q'):10,'None':0}
    piecesValuesBlack = {chess.Piece.from_symbol('p'):1,chess.Piece.from_symbol('r'):5,chess.Piece.from_symbol('n'):3,chess.Piece.from_symbol('b'):3,chess.Piece.from_symbol('q'):10}
    game = board.piece_at(chess.C2)
    whiteSum = 0
    blackSum = 0

    for squareRank in range(8):
        for squareFile in range(8):
            square = board.piece_at(chess.square(squareRank,squareFile))
            if square in piecesValuesWhite:
                whiteSum+=piecesValuesWhite[square]
            elif square in piecesValuesBlack:
                blackSum+=piecesValuesBlack[square]

    return whiteSum-blackSum
