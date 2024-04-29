import uvicorn
import sys
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from src.presentation.controller import (
    controller
)

# version = f"{sys.version_info.major}.{sys.version_info.minor}"

app = FastAPI()
app.include_router(controller.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8000
    # main: ファイル名、app: インスタンス名
    uvicorn.run('main:app', host=host, port=port, reload=True)