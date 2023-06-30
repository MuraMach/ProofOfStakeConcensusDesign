from Game import TicTacToe

class ConsensusMechanism:
    def __init__(self, blockchain):
        self.nodes = []
        self.master_node = None
        self.blockchain = blockchain
    
    def add_node(self, node):
        self.nodes.append(node)
    
    def set_master_node(self, master_node):
        self.master_node = master_node
    
    def play_game(self):
        game = TicTacToe()
        
        while True:
            for node in self.nodes:
                row, col = node.make_move(game.board)
                if game.make_move(row, col):
                    game.print_board()
                    winner = game.check_winner()
                    if winner:
                        if winner == 'Tie':
                            print('It\'s a tie!')
                        else:
                            print(f'{winner} wins!')
                        return
                else:
                    print('Invalid move. Try again.')
    
    def start_consensus(self):
        print('Consensus mechanism started.')
        self.blockchain.print_blockchain_progress()
        self.play_game()
        print('Consensus mechanism finished.')
