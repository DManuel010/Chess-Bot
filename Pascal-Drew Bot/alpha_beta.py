import chess
from evaluation import evaluationFunction


def alpha_beta_search(board, player,depth):

    best_move = None
    infinity = float('inf')
    best_val = -infinity
    beta = infinity
    newBoard = board    # Makes the move on the board copy
    moves = []

    # Creates a list of moves from legal moves
    for move in board.legal_moves:
        moves.append(move)

    for move in moves:
        newBoard.push(move)
        print newBoard.legal_moves
        value = min_value(newBoard, best_val, beta,player,depth)

        if value > best_val:
            best_val = value
            best_move = move

        newBoard.pop()

    return chess.Move.from_uci(str(best_move))



def max_value(gameState, alpha, beta, player,depth):

    if gameState.is_game_over():
        getUtility(gameState,player)

    if depth == 0:
        return evaluationFunction(gameState)

    infinity = float('inf')
    value = -infinity
    newState = gameState

    successors = []
    for move in gameState.legal_moves:
        successors.append(move)

    if len(successors) == 0:
        return evaluationFunction(gameState)

    for state in successors:
        newState.push(state)
        newState.pop()
        value = max(value, min_value(newState, alpha, beta,player,depth-1))

        if value >= beta:
            return value

        alpha = max(alpha, value)
        newState.pop()

    return value



def min_value(gameState, alpha, beta, player,depth):

    if gameState.is_game_over():
        getUtility(gameState,player)

    if depth == 0:
        return evaluationFunction(gameState)

    infinity = float('inf')
    value = infinity
    newState=gameState

    successors = []
    for move in gameState.legal_moves:
        successors.append(move)

    if len(successors) == 0:
        return evaluationFunction(gameState)

    for state in successors:
        newState.push(state)
        value = min(value, max_value(newState, alpha, beta,player,depth-1))

        if value <= alpha:
            return value

        beta = min(beta, value)
        newState.pop()

    return value



def getUtility(gameState,player):

    assert gameState is not None
    return evaluate(gameState,player)
