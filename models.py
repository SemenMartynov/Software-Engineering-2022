from pydantic import BaseModel, constr


class Block(BaseModel):
    hash: str
    data: constr(min_length=256, max_length=256)
    index: int
    prev_hash: str
    nonce: int = 1


class Node(BaseModel):
    blocks_array: list[Block]
    block_index: int | None = None
