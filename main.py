import uvicorn
from config import PORT


if __name__ == "__main__":
    pass
    uvicorn.run("utils:fast_api_application", port=PORT, host='0.0.0.0', reload=True)
