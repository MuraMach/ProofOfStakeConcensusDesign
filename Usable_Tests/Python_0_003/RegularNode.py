from Player import Player

class RegularNode(Player):
    def __init__(self, name, blockchain):
        super().__init__(name)
        self.blockchain = blockchain
    
    def make_move(self, board):
        print(f'{self.name} is making a move.')
        return self.blockchain.solve_block()
