import hashlib
import time
import random

# Define the Block class
class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(data_string.encode()).hexdigest()

# Define the Blockchain class
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0", 0)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        if self.is_valid_block(new_block):
            self.chain.append(new_block)

    def is_valid_block(self, block):
        if block.index != len(self.chain):
            return False

        if block.previous_hash != self.get_latest_block().hash:
            return False

        if block.calculate_hash() != block.hash:
            return False

        return True

    def proof_of_work(self, block):
        target = "0" * 4  # Target difficulty for the Quorum Game consensus
        while block.hash[:4] != target:
            block.nonce += 1
            block.hash = block.calculate_hash()
        return block

# Define the Player class
class Player:
    def __init__(self, symbol):
        self.symbol = symbol
        self.board = None

    def set_board(self, game):
        self.board = game

    def make_move(self):
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if self.board.is_valid_move(row, col):
            return row, col

    def is_game_won(self):
        board = self.board.board
        for row in board:
            if row[0] == row[1] == row[2] != ' ':
                return True
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != ' ':
                return True
        if board[0][0] == board[1][1] == board[2][2] != ' ':
            return True
        if board[0][2] == board[1][1] == board[2][0] != ' ':
            return True
        return False

# Define the QuorumGame class
class QuorumGame:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = None
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def set_current_player(self, player):
        self.current_player = player

    def switch_player(self):
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]

    def display_board(self):
        for row in self.board:
            print("|".join(row))
            print("-----")

    def is_valid_move(self, row, col):
        if row < 0 or row >= 3 or col < 0 or col >= 3:
            return False
        if self.board[row][col] != ' ':
            return False
        return True

    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player.symbol
            if self.is_game_over():
                return True
            self.switch_player()
            return True
        return False

    def is_game_over(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return True

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True

        # Check if the board is full (draw)
        if all(self.board[row][col] != ' ' for row in range(3) for col in range(3)):
            return True

        return False

# Initialize the blockchain and game
blockchain = Blockchain()
game = QuorumGame()

# Create players
player1 = Player('X')
player2 = Player('O')

# Add players to the game
game.add_player(player1)
game.add_player(player2)

# Set the current player
game.set_current_player(player1)

# Set the board for each player
player1.set_board(game)
player2.set_board(game)

# Main game loop
while True:
    # Display the current game board
    game.display_board()

    # Prompt the current player for their move
    print("Player", game.current_player.symbol, "turn:")
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))

    # Make the move and check if the game is over
    if not game.make_move(row, col):
        print("Invalid move. Try again.")
        continue

    if game.is_game_over():
        print("Game over!")
        break

# Print the final blockchain
print("\nFinal Blockchain:")
for block in blockchain.chain:
    print("Block:", block.index)
    print("Data:", block.data)
    print("Hash:", block.hash)
    print()
