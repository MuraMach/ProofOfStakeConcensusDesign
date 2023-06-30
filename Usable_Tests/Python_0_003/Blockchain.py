import random

class Blockchain:
    def __init__(self):
        self.difficulty = 2
        self.blocks = []
        self.pending_transactions = []
        self.block_reward = 10
        self.master_wallet = 'MASTER_WALLET'
        self.regular_wallets = {}
        self.print_blockchain_progress() 

    def print_blockchain_progress(self):
        print('Blockchain is progressing...')
        for _ in range(5):
            self.mine_block()
        print('Blockchain progress complete.')

    def mine_block(self):
        block = {
            'transactions': self.pending_transactions,
            'nonce': random.randint(0, 100),
            'previous_hash': 'PREVIOUS_HASH',
        }
        self.blocks.append(block)
        self.pending_transactions = []
        self.distribute_rewards()

    def distribute_rewards(self):
        total_hash_power = 0.1 * len(self.regular_wallets)
        master_reward = total_hash_power * 0.02

        if len(self.regular_wallets) > 0:
            regular_reward = (total_hash_power - master_reward) / len(self.regular_wallets)
        else:
            regular_reward = 0

        self.regular_wallets[self.master_wallet] = self.regular_wallets.get(self.master_wallet, 0) + master_reward

        for wallet in self.regular_wallets:
            self.regular_wallets[wallet] += regular_reward

    def solve_block(self):
        return random.randint(0, 2), random.randint(0, 2)
