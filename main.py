import uvicorn
# from app import fast_api_application
from fastapi import FastAPI

from models import Node, Block
# from utils import new_blocks_generator, block_handler

fast_api_application = FastAPI(title="Test")
node = Node(blocks_array=[])


# async def start_service():
#     await new_blocks_generator(node)
#
#
# @fast_api_application.post('/')
# async def handler(block: Block):
#     block_handler(node, block)


if __name__ == "__main__":
    pass
    uvicorn.run("utils:fast_api_application", port=6060, host='0.0.0.0', reload=True)
