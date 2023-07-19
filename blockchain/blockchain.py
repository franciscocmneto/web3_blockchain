import hashlib
import json
import time
from flask import Flask, request, jsonify

from flask_cors import CORS



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

CORS(app)

# Dificuldade das blockchains
difficulty_popular = 3
difficulty_vegetarian = 3
difficulty_italian = 3
difficulty_american = 3
difficulty_japanese = 3
difficulty_chinese = 3

# Criação das instâncias das blockchains
blockchain_popular = Blockchain(difficulty_popular)
blockchain_vegetarian = Blockchain(difficulty_vegetarian)
blockchain_italian = Blockchain(difficulty_italian)
blockchain_american = Blockchain(difficulty_american)
blockchain_japanese = Blockchain(difficulty_japanese)
blockchain_chinese = Blockchain(difficulty_chinese)

# Rota para adicionar um novo bloco à blockchain popular
@app.route('/add_block_popular', methods=['POST'])
def add_block_popular():
    data = json.loads(request.data)
    recipes = data['recipes']

    index = len(blockchain_popular.chain)
    timestamp = time.time()
    previous_hash = blockchain_popular.get_latest_block().hash
    nonce = 0

    new_block = Block(index, timestamp, recipes, previous_hash, nonce, blockchain_popular.difficulty)
    blockchain_popular.add_block(new_block)

    response = {'message': 'Block added to popular successfully.'}
    return jsonify(response)

# Rota para obter o estado atual da blockchain popular
@app.route('/get_chain_popular', methods=['GET'])
def get_chain_popular():
    response = {'chain': [block.to_dict() for block in blockchain_popular.chain], 'length': len(blockchain_popular.chain)}
    return jsonify(response)

# Verificar se a blockchain popular é válida
@app.route('/is_valid_popular', methods=['GET'])
def is_valid_popular():
    is_valid = blockchain_popular.is_chain_valid()
    response = {'valid': is_valid}
    return jsonify(response)

# Rota para adicionar um novo bloco à blockchain vegetarian
@app.route('/add_block_vegetarian', methods=['POST'])
def add_block_vegetarian():
    data = json.loads(request.data)
    recipes = data['recipes']

    index = len(blockchain_vegetarian.chain)
    timestamp = time.time()
    previous_hash = blockchain_vegetarian.get_latest_block().hash
    nonce = 0

    new_block = Block(index, timestamp, recipes, previous_hash, nonce, blockchain_vegetarian.difficulty)
    blockchain_vegetarian.add_block(new_block)

    response = {'message': 'Block added to vegetarian successfully.'}
    return jsonify(response)

# Rota para obter o estado atual da blockchain vegetarian
@app.route('/get_chain_vegetarian', methods=['GET'])
def get_chain_vegetarian():
    response = {'chain': [block.to_dict() for block in blockchain_vegetarian.chain], 'length': len(blockchain_vegetarian.chain)}
    return jsonify(response)

# Verificar se a blockchain vegetarian é válida
@app.route('/is_valid_vegetarian', methods=['GET'])
def is_valid_vegetarian():
    is_valid = blockchain_vegetarian.is_chain_valid()
    response = {'valid': is_valid}
    return jsonify(response)

# Rota para adicionar um novo bloco à blockchain italian
@app.route('/add_block_italian', methods=['POST'])
def add_block_italian():
    data = json.loads(request.data)
    recipes = data['recipes']

    index = len(blockchain_italian.chain)
    timestamp = time.time()
    previous_hash = blockchain_italian.get_latest_block().hash
    nonce = 0

    new_block = Block(index, timestamp, recipes, previous_hash, nonce, blockchain_italian.difficulty)
    blockchain_italian.add_block(new_block)

    response = {'message': 'Block added to italian successfully.'}
    return jsonify(response)

# Rota para obter o estado atual da blockchain italian
@app.route('/get_chain_italian', methods=['GET'])
def get_chain_italian():
    response = {'chain': [block.to_dict() for block in blockchain_italian.chain], 'length': len(blockchain_italian.chain)}
    return jsonify(response)

# Verificar se a blockchain italian é válida
@app.route('/is_valid_italian', methods=['GET'])
def is_valid_italian():
    is_valid = blockchain_italian.is_chain_valid()
    response = {'valid': is_valid}
    return jsonify(response)

# Rota para adicionar um novo bloco à blockchain american
@app.route('/add_block_american', methods=['POST'])
def add_block_american():
    data = json.loads(request.data)
    recipes = data

    index = len(blockchain_american.chain)
    timestamp = time.time()
    previous_hash = blockchain_american.get_latest_block().hash
    nonce = 0

    new_block = Block(index, timestamp, recipes, previous_hash, nonce, blockchain_american.difficulty)
    blockchain_american.add_block(new_block)

    response = {'message': 'Block added to american successfully.'}
    return jsonify(response)

# Rota para obter o estado atual da blockchain american
@app.route('/get_chain_american', methods=['GET'])
def get_chain_american():
    response = {'chain': [block.to_dict() for block in blockchain_american.chain], 'length': len(blockchain_american.chain)}
    return jsonify(response)

# Verificar se a blockchain american é válida
@app.route('/is_valid_american', methods=['GET'])
def is_valid_american():
    is_valid = blockchain_american.is_chain_valid()
    response = {'valid': is_valid}
    return jsonify(response)

# Rota para adicionar um novo bloco à blockchain japanese
@app.route('/add_block_japanese', methods=['POST'])
def add_block_japanese():
    data = json.loads(request.data)
    recipes = data['recipes']

    index = len(blockchain_japanese.chain)
    timestamp = time.time()
    previous_hash = blockchain_japanese.get_latest_block().hash
    nonce = 0

    new_block = Block(index, timestamp, recipes, previous_hash, nonce, blockchain_japanese.difficulty)
    blockchain_japanese.add_block(new_block)

    response = {'message': 'Block added to japanese successfully.'}
    return jsonify(response)

# Rota para obter o estado atual da blockchain japanese
@app.route('/get_chain_japanese', methods=['GET'])
def get_chain_japanese():
    response = {'chain': [block.to_dict() for block in blockchain_japanese.chain], 'length': len(blockchain_japanese.chain)}
    return jsonify(response)

# Verificar se a blockchain japanese é válida
@app.route('/is_valid_japanese', methods=['GET'])
def is_valid_japanese():
    is_valid = blockchain_japanese.is_chain_valid()
    response = {'valid': is_valid}
    return jsonify(response)

# Rota para adicionar um novo bloco à blockchain chinese
@app.route('/add_block_chinese', methods=['POST'])
def add_block_chinese():
    data = json.loads(request.data)
    recipes = data['recipes']

    index = len(blockchain_chinese.chain)
    timestamp = time.time()
    previous_hash = blockchain_chinese.get_latest_block().hash
    nonce = 0

    new_block = Block(index, timestamp, recipes, previous_hash, nonce, blockchain_chinese.difficulty)
    blockchain_chinese.add_block(new_block)

    response = {'message': 'Block added to chinese successfully.'}
    return jsonify(response)

# Rota para obter o estado atual da blockchain chinese
@app.route('/get_chain_chinese', methods=['GET'])
def get_chain_chinese():
    response = {'chain': [block.to_dict() for block in blockchain_chinese.chain], 'length': len(blockchain_chinese.chain)}
    return jsonify(response)

# Verificar se a blockchain chinese é válida
@app.route('/is_valid_chinese', methods=['GET'])
def is_valid_chinese():
    is_valid = blockchain_chinese.is_chain_valid()
    response = {'valid': is_valid}
    return jsonify(response)

# Execução do aplicativo Flask
if __name__ == '__main__':
    app.run(port=5000)