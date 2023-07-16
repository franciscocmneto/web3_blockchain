import hashlib
import json
import time
from flask import Flask, request, jsonify

# Classe para representar um bloco na blockchain
class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce, difficulty):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.difficulty = difficulty
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(data.encode()).hexdigest()

    def mine_block(self):
        target = "0" * self.difficulty
        while self.hash[:self.difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

    def to_dict(self):
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
            "difficulty": self.difficulty,
            "hash": self.hash
        }

# Classe para representar a blockchain
class Blockchain:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        index = 0
        timestamp = time.time()
        data = "Genesis Block"
        previous_hash = "0"
        nonce = 0

        block = Block(index, timestamp, data, previous_hash, nonce, self.difficulty)
        block.mine_block()
        
        return block

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block()
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

# Criação da instância do Flask
app = Flask(__name__)

# Dificuldade da blockchain
difficulty = 3

# Criação da instância da blockchain
blockchain = Blockchain(difficulty)

# Rota para adicionar um novo bloco à blockchain
@app.route('/add_block', methods=['POST'])
def add_block():
    data = json.loads(request.data)
    message1 = data['message1']
    message2 = data['message2']

    index = len(blockchain.chain)
    timestamp = time.time()
    previous_hash = blockchain.get_latest_block().hash
    nonce = 0

    new_block = Block(index, timestamp, [message1, message2], previous_hash, nonce, blockchain.difficulty)
    blockchain.add_block(new_block)

    response = {'message': 'Block added successfully.'}
    return jsonify(response)

# Rota para obter o estado atual da blockchain
@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {'chain': [block.to_dict() for block in blockchain.chain], 'length': len(blockchain.chain)}
    return jsonify(response)

# Verificar se a blockchain é válida
@app.route('/is_valid', methods=['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid()
    response = {'valid': is_valid}
    return jsonify(response)

# Execução do aplicativo Flask
if __name__ == '__main__':
    app.run(port=5000)
