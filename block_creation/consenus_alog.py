from flask import Flask
from flask import  request
import  requests

from block_chain import *
from snakecoin_transaction import *
import  json
node = Flask(__name__)

@node.route('/blocks',methods=['GET'])

def get_blocks():
    chain_to_send = blockchain

    for block in chain_to_send:
        block_index = str(block.index)
        block_timestamp = str(block.timestamp)
        block_data = str(block.data)
        block_hash = str(block.hash)

        block = {"index": block_index,
      "timestamp": block_timestamp,
      "data": block_data,
      "hash": block_hash
    }

    chain_to_send = json.dumps(chain_to_send)
    return  chain_to_send


peer_nodes = []
def find_new_chains():
    other_chains = []
    for node_url in peer_nodes:
        block = requests.get(node_url + "/blocks").content

        block = json.loads(block)

        other_chains.append(block)

    return  other_chains


def consensus():
    other_chains = find_new_chains()


    longest_chain = blockchain
    for chain in other_chains:
        if len(longest_chain) < len(chain):
            longest_chain = chain

    blockchain = longest_chain