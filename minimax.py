import chess
import random

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
        if gameState.is_game_over(): return evaluate(gameState, player)
        if depth==0: return 0
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
            return evaluate(gameState, player)
        if depth == 0:
            return 0
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
