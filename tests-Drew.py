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
        else:
            currentPlayer = players[1]

        board.push(randomAI(board))

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



def pascalMinimax(board,depth):
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
        score = mini(newBoard, depth)
        if score > best_score:
            best_move = move
            best_score = score
        newBoard.pop() #undos last move
    return chess.Move.from_uci(str(best_move))



def maxi(gameState, depth):
        if gameState.is_game_over(): return evaluate(gameState)
        if depth==0: return 0
        maxScore = -99999
        newBoard = gameState
        #Generates a list of moves from legal moves
        moves = []
        for move in gameState.legal_moves:
            moves.append(move)
        #Executes max function
        for move in moves:
            newBoard.push(move)
            score = mini(newBoard, depth-1) #Calls min function
            if score > maxScore:
                maxScore = score
            newBoard.pop() #undos last move
        return maxScore



def mini(gameState, depth):
        if gameState.is_game_over(): return evaluate(gameState)
        if depth ==0: return 0
        minScore = 99999
        newBoard = gameState
        #Generates a list of moves from legal moves
        moves = []
        for move in gameState.legal_moves:
            moves.append(move)
        #Executes max function
        for move in moves:
            newBoard.push(move)
            score = maxi(newBoard, depth-1) #Calls min function
            if score < minScore:
                minScore = score
            newBoard.pop() #undos last move
        return minScore



    #Evaluates terminal state
def evaluate(board):
        if (board.is_stalemate() or board.is_insufficient_material() or
            board.can_claim_threefold_repetition() or board.can_claim_fifty_moves() or
            board.can_claim_draw()):
            return 0
        else: return 10


def main():

    drewTest()

main()
