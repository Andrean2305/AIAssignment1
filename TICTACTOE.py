import math
import copy

class TicTacToe:
    def __init__(self, state=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]):
        self.state = state

    def make_move(self, row, col, val):
        if 0 <= row < 3 and 0 <= col < 3 and self.state[row][col] == 0:
            self.state[row][col] = val
            return True
        return False

    def try_move(self, state, row, col, val):
        if 0 <= row < 3 and 0 <= col < 3 and state[row][col] == 0:
            state[row][col] = val
        return state

    def terminal_node(self, state):
        result = 0
        is_game_over = False

        empty_cells = False
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    empty_cells = True

        for i in range(3):
            sum_p1 = 0
            sum_p2 = 0
            for j in range(3):
                if state[i][j] == 1:
                    sum_p1 += 1
                if state[i][j] == -1:
                    sum_p2 += -1
            if sum_p1 == 3 or sum_p2 == -3:
                is_game_over = True
                if sum_p1 == 3:
                    result = 10
                if sum_p2 == -3:
                    result = -10

        for j in range(3):
            sum_p1 = 0
            sum_p2 = 0
            for i in range(3):
                if state[i][j] == 1:
                    sum_p1 += 1
                if state[i][j] == -1:
                    sum_p2 += -1
            if sum_p1 == 3 or sum_p2 == -3:
                is_game_over = True
                if sum_p1 == 3:
                    result = 10
                if sum_p2 == -3:
                    result = -10

        sum_p1 = 0
        sum_p2 = 0
        for i in range(3):
            if state[i][i] == 1:
                sum_p1 += 1
            if state[i][i] == -1:
                sum_p2 += -1
        if sum_p1 == 3 or sum_p2 == -3:
            is_game_over = True
            if sum_p1 == 3:
                result = 10
            if sum_p2 == -3:
                result = -10

        sum_p1 = 0
        sum_p2 = 0
        for i in range(3):
            if state[i][2 - i] == 1:
                sum_p1 += 1
            if state[i][2 - i] == -1:
                sum_p2 += -1
        if sum_p1 == 3 or sum_p2 == -3:
            is_game_over = True
            if sum_p1 == 3:
                result = 10
            if sum_p2 == -3:
                result = -10

        is_game_over = is_game_over or not empty_cells
        return {"game_over": is_game_over, "result": result}

    def expand_state(self, state):
        children = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    child = [i, j]
                    children.append(child)
        return children

    def alphabeta(self, state, depth, alpha, beta, is_max_player):
        if depth == 0 or self.terminal_node(state)["game_over"]:
            return self.terminal_node(state)["result"]

        if is_max_player:
            v_max = -math.inf
            children = self.expand_state(state)
            for pos in children:
                child = copy.deepcopy(state)
                child[pos[0]][pos[1]] = 1
                v = self.alphabeta(child, depth - 1, alpha, beta, not is_max_player)
                v_max = max(v_max, v)
                alpha = max(alpha, v)
                if beta <= alpha:
                    break
            return v_max
        else:
            v_min = math.inf
            children = self.expand_state(state)
            for pos in children:
                child = copy.deepcopy(state)
                child[pos[0]][pos[1]] = -1
                v = self.alphabeta(child, depth - 1, alpha, beta, not is_max_player)
                v_min = min(v_min, v)
                beta = min(beta, v)
                if beta <= alpha:
                    break
            return v_min

    def computer_move(self):
        depth = 9  # Maximum depth for Alpha-Beta
        alpha = -math.inf
        beta = math.inf
        is_max_player = True
        best_move = None
        best_value = -math.inf

        for move in self.expand_state(self.state):
            child = copy.deepcopy(self.state)
            child[move[0]][move[1]] = 1  # Simulate a computer move
            value = self.alphabeta(child, depth - 1, alpha, beta, not is_max_player)

            if value > best_value:
                best_value = value
                best_move = move

        self.make_move(best_move[0], best_move[1], 1)  # Make the best computer move

    def print_board(self):
        for row in self.state:
            print(" ".join(["X" if cell == 1 else "O" if cell == -1 else "-" for cell in row]))

    def play_game(self):
        while True:
            self.print_board()
            row = int(input("Enter the row (0, 1, 2) for your move: "))
            col = int(input("Enter the column (0, 1, 2) for your move: "))
            if self.make_move(row, col, -1):
                if self.terminal_node(self.state)["game_over"]:
                    self.print_board()
                    result = self.terminal_node(self.state)["result"]
                    if result == 10:
                        print("Computer wins!")
                    elif result == -10:
                        print("You win!")
                    else:
                        print("It's a tie!")
                    break
                self.computer_move()
                if self.terminal_node(self.state)["game_over"]:
                    self.print_board()
                    result = self.terminal_node(self.state)["result"]
                    if result == 10:
                        print("Computer wins!")
                    elif result == -10:
                        print("You win!")
                    else:
                        print("It's a tie!")
                    break

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
    
#SOURCE SIR ZANDOS GITHUB //MODIFY BY A.H. 
#FEEL FREE TO MODIFY AND USE THIS CODE
