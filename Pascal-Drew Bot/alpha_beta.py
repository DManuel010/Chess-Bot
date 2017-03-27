import chess
from evaluation import evaluationFunction


import chess
from evaluation import evaluationFunction
import chess.polyglot


def alpha_beta_search(board, player,theDepth):

        PLAYER = player
        OPPONENT = None
        if player=="white":
            PLAYER = "white"
            OPPONENT = "black"
        else:
            PLAYER = "black"
            OPPONENT ="white"
        def max_agent(state, depth, alpha, beta):
            if state.is_game_over():
                return evaluationFunction(state,OPPONENT,PLAYER)
            moves = getLegalMoves(state)
            best_score = float("-inf")
            score = best_score
            best_move = None
            for move in moves:
                newBoard = state.copy()

                newBoard.push(chess.Move.from_uci(str(move)))
                #print newBoard
                score = min_agent(newBoard, depth, alpha, beta)
                newBoard.pop()
                if score > best_score:
                    best_score = score
                    best_move = move
                alpha = max(alpha, best_score)
                if best_score > beta:
                    return best_score
            if depth == 0:
                return chess.Move.from_uci(str(best_move))
            else:
                return best_score

        def min_agent(state, depth, alpha, beta):
            if state.is_game_over():
                return evaluationFunction(state,PLAYER,PLAYER)
            moves = getLegalMoves(state)
            best_score = float("inf")
            score = best_score
            for move in moves:
                if depth == theDepth - 1:
                    newBoard = state.copy()
                    newBoard.push(chess.Move.from_uci(str(move)))
                    score = evaluationFunction(newBoard,OPPONENT,PLAYER)
                    newBoard.pop()
                else:
                    newBoard = state.copy()
                    newBoard.push(chess.Move.from_uci(str(move)))
                    #print newBoard
                    score = evaluationFunction(newBoard,OPPONENT,PLAYER)
                    score = max_agent(newBoard, depth + 1, alpha, beta)
                    newBoard.pop()

                if score < best_score:
                    best_score = score
                beta = min(beta, best_score)
                if best_score < alpha:
                    return best_score
            return best_score

        best_move = None
        best_weight = None
        try:
            with chess.polyglot.open_reader("/Users/pascal/Desktop/Chess-Bot1/Pascal-Drew Bot/gm2001.bin") as reader:
                for entry in reader.find_all(board):
                    if entry.weight>best_weight:
                        best_weight=entry.weight
                        best_move=entry.move()
                if best_move!=None:
                    print "opening move", best_move
                    return best_move
                else:
                    print "max agent"
                    return max_agent(board, 0, float("-inf"), float("inf"))
        except IndexError:
            print "Index Error"

def getLegalMoves(board):
        moves = []
        for move in board.legal_moves:
            moves.append(move)
        return moves



def getUtility(gameState,player):

    assert gameState is not None
    return evaluate(gameState,player)


def stockFish(board):
    engine = chess.uci.popen_engine("/Users/pascal/Desktop/Chess-Bot1/Pascal-Drew Bot/Stockfish/src/stockfish")
    engine.uci()
    engine.position(board)
    best_move, ponder_move = engine.go(movetime=5000)
    return best_move
