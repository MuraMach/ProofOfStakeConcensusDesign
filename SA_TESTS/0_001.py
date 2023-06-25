########
THIS WILL NOT WORK IF YOU DON'T KNOW HOW TO USE IT. IT IS ONLY AN EXAMPLE AND FOR RESEARCH PURPOSES. PLEASE REFER TO PAPER AND CODE DESIGN IN ORDER TO UNDERSTAND THIS IN ANY WAY WHATSOEVER.
########


# Import required libraries
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

# Define the Game class
class Game:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

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
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
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
game = Game()

# Main game loop
while True:
    # Display the current game board
    game.display_board()

    # Prompt the current player for their move
    print("Player", game.current_player, "turn:")
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))

    # Make the move and check if the game is over
    if game.make_move(row, col):
        if game.is_game_over():
            # Game is over, create a new block and add it to the blockchain
            latest_block = blockchain.get_latest_block()
            new_block = Block(latest_block.index + 1, time.time(), game.board, latest_block.hash, 0)
            new_block = blockchain.proof_of_work(new_block)
            blockchain.add_block(new_block)
            print("Game over! Block added to the blockchain.")
            break
    else:
        print("Invalid move. Try again.")

# Print the final blockchain
print("\nFinal Blockchain:")
for block in blockchain.chain:
    print("Block:", block.index)
    print("Data:", block.data)
    print("Hash:", block.hash)
    print()
