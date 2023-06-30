from Consensus import ConsensusMechanism
from RegularNode import RegularNode
from MasterNode import MasterNode
from Blockchain import Blockchain

# Create a blockchain instance
blockchain = Blockchain()

# Create regular nodes
node1 = RegularNode("Node1", blockchain)
node2 = RegularNode("Node2", blockchain)
node3 = RegularNode("Node3", blockchain)

# Create the master node
master_node = MasterNode("MasterNode", blockchain)

# Add regular nodes to the consensus mechanism
consensus = ConsensusMechanism(blockchain)
consensus.add_node(node1)
consensus.add_node(node2)
consensus.add_node(node3)

# Set the master node for the consensus mechanism
consensus.set_master_node(master_node)

# Add regular wallets
blockchain.regular_wallets["Node1"] = 0
blockchain.regular_wallets["Node2"] = 1
blockchain.regular_wallets["Node3"] = 2

# Start the consensus mechanism
consensus.start_consensus()
