from fastapi import FastAPI, WebSocket
import uvicorn
from typing import List
from fastapi.middleware.cors import CORSMiddleware

connections: List[WebSocket] = []
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.websocket("/ws/logs")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connections.append(websocket)
    try:
        while True:
            await websocket.receive_text()
    except Exception as e:
        connections.remove(websocket)
        await websocket.close()

async def broadcast_message(message: str):
    for connection in connections:
        await connection.send_text(message)

if __name__ == "__main__":
    uvicorn.run(app)
