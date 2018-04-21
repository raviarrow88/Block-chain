from block import Block
from genesis_block import create_genesis_block
from next_block import next_block

blockchain = [create_genesis_block()]
previous_block = blockchain[0]

number_of_blocks_to_add = 10

for i in range(0,number_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print "Block #{} has been added to the blockchain!".format(block_to_add.index)
    print "Hash: {}\n".format(block_to_add.hash)
    print "data: {}\n".format(block_to_add.data)
    # print "index:{}".format(block_to_add.index)