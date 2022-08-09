from datetime import datetime
from hashlib import sha256  # Secure Hash Algorithm


class Block:
    def __init__(self, transactions, previous_hash, nonce=0):
        self.timestamp = datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.generate_hash()

    def print_block(self):
        # print block contents
        print("timestamp: ", self.timestamp)
        print("transaction: ", self.transactions)
        print("current hash: ", self.generate_hash())

    def generate_hash(self):
        # hash the block contents
        block_contents = str(self.timestamp) + str(self.transactions) + \
            str(self.previous_hash) + str(self.nonce)

        block_hash = sha256(block_contents.encode())
        return block_hash.hexdigest()


class BlockChain:
    def __init__(self):
        self.chain = []
        self.all_transactions = []
        self.genesis_block()

    def genesis_block(self):
        transactions = {}
        genesis_block = Block(transactions, "0")
        self.chain.append(genesis_block)
        return self.chain

  # prints contents of blockchain
    def print_blocks(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print("Block {} {}".format(i, current_block))
            current_block.print_block()

    # add block to blockchain `chain`
    def add_block(self, transactions):
        previous_block_hash = self.chain[len(self.chain)-1].hash
        new_block = Block(transactions, previous_block_hash)
        self.chain.append(new_block)

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if(current.hash != current.generate_hash()):
                print(
                    "The current hash of the block does not equal the generated hash of the block.")
                return False
            if(current.previous_hash != previous.generate_hash()):
                print(
                    "The previous block's hash does not equal the previous hash value stored in the current block.")
                return False
        return True


new_transactions = [{'amount': '30', 'sender': 'alice', 'receiver': 'bob'},
                    {'amount': '55', 'sender': 'bob', 'receiver': 'alice'}]


my_blockchain = BlockChain()
my_blockchain.add_block(new_transactions)
my_blockchain.print_blocks()
my_blockchain.chain[1].transactions = 'fake_transactions'
my_blockchain.validate_chain()
new_transactions = [{'amount': '30', 'sender': 'alice', 'receiver': 'bob'},
                    {'amount': '55', 'sender': 'bob', 'receiver': 'alice'}]

# sets the amount of leading zeros that must be found in the hash produced by the nonce
difficulty = 2
nonce = 0  # default starting value

# creating the proof
proof = sha256((str(nonce)+str(new_transactions)).encode()).hexdigest()
# printing proof
print(proof)

# finding a proof that has 2 leading zeros
while (proof[:2] != '0' * difficulty):
    nonce += 1
    proof = sha256((str(nonce) + str(new_transactions)).encode()).hexdigest()

# printing final proof that was found
final_proof = proof
print(final_proof)
