import math

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def display_board(self):
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("-" * 9)
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("-" * 9)
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  
            (0, 4, 8), (2, 4, 6) 
        ]
        
        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                return self.board[a]
        
        if ' ' not in self.board:
            return 'Tie'
        
        return None

    def minimax(self, depth, maximizing_player, alpha, beta):
        winner = self.check_winner()
        if winner == 'X':
            return -10 + depth
        elif winner == 'O':
            return 10 - depth
        elif winner == 'Tie':
            return 0

        if maximizing_player:
            max_eval = -math.inf
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'O'
                    eval = self.minimax(depth + 1, False, alpha, beta)
                    self.board[i] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            return max_eval
        else:
            min_eval = math.inf
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'X'
                    eval = self.minimax(depth + 1, True, alpha, beta)
                    self.board[i] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return min_eval

    def get_best_move(self):
        best_move = None
        best_value = -math.inf
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                move_value = self.minimax(0, False, -math.inf, math.inf)
                self.board[i] = ' '
                if move_value > best_value:
                    best_value = move_value
                    best_move = i
        return best_move

    def play(self):
        while True:
            self.display_board()
            winner = self.check_winner()
            if winner:
                self.display_board()
                if winner == 'Tie':
                    print("It's a tie!")
                else:
                    print(f"{winner} wins!")
                break

            if self.current_player == 'X':
                position = int(input("Enter your move (0-8): "))
                if not self.make_move(position):
                    print("Invalid move. Try again.")
            else:
                best_move = self.get_best_move()
                self.make_move(best_move)
                print(f"AI plays at position {best_move}")

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
