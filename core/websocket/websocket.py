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
            data = await websocket.receive()
            if data["type"] == "websocket.receive":
                if data["text"] == "ping":
                    await websocket.send_text("pong")
                else:
                    print('data type not accounted for yet, cant parse. Data: ', data)
                    pass

            elif data["type"] == "websocket.disconnect":
                break
    except Exception as e:
        # Log the error if needed
        print('error', e)
        pass
    finally:
        connections.remove(websocket)
        await websocket.close()

async def broadcast_message(message: str):
    disconnected_sockets = []
    for connection in connections:
        try:
            await connection.send_text(message)
        except Exception:
            # If there's an error, assume the socket is disconnected
            disconnected_sockets.append(connection)
    for socket in disconnected_sockets:
        connections.remove(socket)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
