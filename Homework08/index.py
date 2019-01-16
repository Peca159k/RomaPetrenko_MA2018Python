#The task was to make the game for 0,
#but I made the game for Õ.
#Need something new
# GL HF
import random
import poc_ttt_gui
import poc_ttt_provided as provided

NTRIALS = 100 
SCORE_CURRENT = 1.0 
SCORE_OTHER = 1.0  

def mc_trial(board, player):
    #full game
    while not board.check_win():
        next_move = random.choice(board.get_empty_squares())
        board.move(next_move[0], next_move[1], player)
        player = provided.switch_player(player)
    #
def mc_update_scores(scores, board, player):
    draw = True
    scores_list = [0, SCORE_CURRENT, SCORE_OTHER]      
    if board.check_win() == player or board.check_win() == provided.switch_player(player):
        scores_list[provided.switch_player(board.check_win()) -1] *= (-1)
        draw = False
    if not draw:
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                scores[row][col] += scores_list[board.square(row, col) -1]
    #
def get_best_move(board, scores):
    best_moves = []
    for empty_sq in board.get_empty_squares():
        if best_moves:
            if scores[empty_sq[0]][empty_sq[1]] > scores[best_moves[0][0]][best_moves[0][1]]:
                best_moves = []
                best_moves.append(empty_sq)
            elif scores[empty_sq[0]][empty_sq[1]] == scores[best_moves[0][0]][best_moves[0][1]]:
                best_moves.append(empty_sq)
        else:
            best_moves.append(empty_sq)
    if best_moves:
        return random.choice(best_moves)
    #
def mc_move(board, player, trials):
    score_len = board.get_dim()
    scores = [[0 for dummy_row in range(score_len)] for dummy_col in range(score_len)]
    for dummy_trials in range(trials):
        temp_board = board.clone()
        mc_trial(temp_board, player)
        mc_update_scores(scores, temp_board, player)
    return get_best_move(board, scores)    
    #  
poc_ttt_gui.run_gui(3, provided.PLAYERO, mc_move, NTRIALS, False)
