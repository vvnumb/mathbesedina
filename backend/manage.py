from uvicorn import run

from config import uvicorn_config


if __name__ == "__main__":
    run(**uvicorn_config.dict())
