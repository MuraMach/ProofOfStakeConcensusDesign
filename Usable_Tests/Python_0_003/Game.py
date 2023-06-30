class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
    
    def print_board(self):
        print('---------')
        for row in self.board:
            print('|', end='')
            for cell in row:
                print(f' {cell} ', end='|')
            print('\n---------')
    
    def make_move(self, row, col):
        if row < 0 or row > 2 or col < 0 or col > 2:
            return False
        
        if self.board[row][col] != ' ':
            return False
        
        self.board[row][col] = 'X'
        return True
    
    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        # Check for a tie
        if all(self.board[i][j] != ' ' for i in range(3) for j in range(3)):
            return 'Tie'
        
        return None
