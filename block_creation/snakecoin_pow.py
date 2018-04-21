

import  datetime as date
import json
from block import Block
from block_chain import *
from snakecoin_transaction import *
miner_address = "q3nf394hjg-random-miner-address-34nf3i4nflkn3oi"
from flask import Flask

node = Flask(__name__)

def proof_of_work(last_proof):

    incrementor = last_proof +1

    while not (incrementor % 9 ==0 and incrementor%last_proof ==0 ):
        incrementor +=1

    return  incrementor




@node.route('/mine',methods=['GET'])
def mine():
    last_block = blockchain[len(blockchain)-1]
    last_proof = last_block.data['proof-of-work']

    proof = proof_of_work(last_proof)

    current_node_transactions.append(
        {"from": "network", "to": miner_address, "amount": 1}
    )


    new_block_data = {
    "proof-of-work": proof,
    "transactions": list(current_node_transactions)
     }

    new_block_index = last_block.index+1
    new_block_timestamp = this_timestamp = date.datetime.now()
    last_block_hash = last_block.hash

    mined_block = Block(
        new_block_index,
        new_block_timestamp,
        new_block_data,
        last_block_hash,

    )

    blockchain.append(mined_block)
    # Let the client know we mined a block
    return json.dumps({
        "index": new_block_index,
        "timestamp": str(new_block_timestamp),
        "data": new_block_data,
        "hash": last_block_hash
    }) + "\n"