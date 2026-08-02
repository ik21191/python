from fastapi_demo.models.user_models import SignupDetails
from fastapi import APIRouter, FastAPI, Request, status, WebSocket, WebSocketDisconnect
import logging

log = logging.getLogger(__name__)

class WebsocketManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        log.info(f'WebSocket connected: {websocket}')
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        log.info(f'WebSocket disconnected: {websocket}')
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        log.info(f'Broadcasting message: {message}')
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except Exception:
                # Handle edge case where client dropped silently
                pass

websocket_manager = WebsocketManager()


        

