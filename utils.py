import random
import string
from asyncio import sleep
from hashlib import sha256

import grequests
from fastapi import FastAPI

from config import PORT, NODE_LIST
from models import Node, Block


def generate_random_data(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for _ in range(length))
    return rand_string


def get_block_hash(block: Block):
    current_string = str(block.index) + block.prev_hash + block.data + str(block.nonce)
    current_hash = sha256(current_string.encode('utf-8'))
    return current_hash


def mine_block(block: Block):
    current_hash = get_block_hash(block)

    while current_hash.hexdigest()[-4:] != "0000":
        block.nonce += random.randint(1, 30)
        current_hash = get_block_hash(block)
    block.hash = current_hash.hexdigest()
    return block


def create_block(index: int, prev_hash: str):
    block = Block(
        hash="",
        data=generate_random_data(256),
        index=index,
        prev_hash=prev_hash,
        nonce=1,
    )
    block = mine_block(block)
    return block


def create_genesis():
    return create_block(0, "GENESIS")


def block_handler(node: Node, received_block: Block):
    if received_block.index == 0:
        node.blocks_array.append(received_block)
        node.block_index = 0
        print(f"Block with hash {received_block.hash} saved")
        return True

    last_block_index = node.blocks_array[-1].index
    if received_block.index > last_block_index:
        node.blocks_array.append(received_block)
        node.block_index = received_block.index
        print(f"Block with hash {received_block.hash} saved")
        return True

    print(f"Block with hash {received_block.hash} not saved")
    return False


async def generate_new_block(node: Node):
    if len(node.blocks_array) == 0:
        if 'node1' not in NODE_LIST:
            new_block = create_genesis()
            return new_block
    else:
        new_block = mine_block(create_block(node.block_index + 1, node.blocks_array[-1].hash))
        return new_block


async def new_blocks_generator(node: Node):
    while True:
        new_block = await generate_new_block(node)

        if new_block is not None and (node.block_index is None or new_block.index > node.block_index):
            block_handler(node, new_block)

            rst = (grequests.post(f"http://{node_name}:{PORT}/", json=new_block) for node_name in NODE_LIST)
            grequests.map(rst)

        await sleep(0.2)


fast_api_application = FastAPI(title="Test")
node = Node(blocks_array=[])


async def start_service():
    await new_blocks_generator(node)


@fast_api_application.post('/')
async def handler(block: Block):
    block_handler(node, block)


fast_api_application.add_event_handler('startup', start_service)
