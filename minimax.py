import chess
import chess.uci
import random
from pascalH import pascalHueristic

def pascalMinimax(board,depth,player):
    best_move = None
    best_score = -9999
    newBoard = board #Makes the move on the board copy
    moves = []
    #Creates a list of moves from legal moves
    for move in board.legal_moves:
        moves.append(move)
    #Executes minimax function
    for move in moves:
        newBoard.push(move)
        score = mini(newBoard, depth, player)
        if score > best_score:
            best_move = move
            best_score = score
        newBoard.pop() #undos last move
    return chess.Move.from_uci(str(best_move))



def maxi(gameState, depth, player):
        if gameState.is_game_over(): return evaluate(gameState, "black")
        if depth==0: return pascalHueristic(gameState)
        maxScore = -99
        newBoard = gameState
        #Generates a list of moves from legal moves
        moves = []
        for move in gameState.legal_moves:
            moves.append(move)
        #Executes max function
        for move in moves:
            newBoard.push(move)
            score = mini(newBoard, depth-1, player) #Calls min function
            if score > maxScore:
                maxScore = score
            newBoard.pop() #undos last move
        return maxScore



def mini(gameState, depth, player):
        if gameState.is_game_over():
            return evaluate(gameState, "white")
        if depth == 0:
            return pascalHueristic(gameState)
        minScore = 99
        newBoard = gameState
        #Generates a list of moves from legal moves
        moves = []
        for move in gameState.legal_moves:
            moves.append(move)
        #Executes max function
        for move in moves:
            newBoard.push(move)
            score = maxi(newBoard, depth-1, player) #Calls min function
            if score < minScore:
                minScore = score
            newBoard.pop() #undos last move
        return minScore



    #Evaluates terminal state
def evaluate(board, player):

        if (board.is_stalemate() or board.is_insufficient_material() or
            board.can_claim_threefold_repetition() or board.can_claim_fifty_moves() or
            board.can_claim_draw()):
            return 0

        if player == "white":
            return 999

        else:
            return -999


def alpha_beta_search(board, player,depth):
        best_move = None
        infinity = float('inf')
        best_val = -infinity
        beta = infinity
        newBoard = board #Makes the move on the board copy
        moves = []
        #Creates a list of moves from legal moves
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
        if depth==0:
            return pascalHueristic(gameState)
        infinity = float('inf')
        value = -infinity
        newState=gameState
        successors= []
        for move in gameState.legal_moves:
            successors.append(move)
        if len(successors)==0:
            return pascalHueristic(gameState)
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
        if depth==0:
            return pascalHueristic(gameState)
        infinity = float('inf')
        value = infinity
        newState=gameState
        successors= []
        for move in gameState.legal_moves:
            successors.append(move)
        if len(successors)==0:
            return pascalHueristic(gameState)
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
