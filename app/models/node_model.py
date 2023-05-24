from pydantic import BaseModel

from app.models.block_model import Block


class Node(BaseModel):
    blocks_array: list[Block]
    block_index: int | None = None
