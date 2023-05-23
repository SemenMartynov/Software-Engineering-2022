import random
import string
from hashlib import sha256

from app.models.block_model import Block


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
    block.hash = current_hash
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
