from asyncio import sleep

import grequests as grequests

from app.models.block_model import Block
from app.models.node_model import Node
from app.utils.block_utils import create_genesis, create_block
from config import NODE_LIST


def block_handler(node: Node, received_block: Block):
    if received_block.index == 0:
        node.blocks_array.append(received_block)
        node.block_index = 0
        return True

    last_block_index = node.blocks_array[-1].index
    if received_block.index > last_block_index:
        node.blocks_array.append(received_block)
        node.block_index = received_block.index
        return True

    return False


async def generate_new_block(node: Node):
    if len(node.blocks_array) == 0:
        if 'node1' not in NODE_LIST:
            new_block = create_genesis()
            return new_block
    else:
        new_block = create_block(node.block_index+1, node.blocks_array[-1].hash)
        return new_block


async def new_blocks_generator(node: Node):
    while True:
        new_block = await generate_new_block(node)
        if new_block.index > node.block_index:
            block_handler(node, new_block)

            rst = (grequests.post(f"http://{node_name}:5050/", json=new_block) for node_name in NODE_LIST)
            grequests.map(rst)

        await sleep(0.2)


def start_node():
    pass
