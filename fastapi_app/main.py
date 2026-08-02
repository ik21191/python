from fastapi import FastAPI, Request, status, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi_demo.config import log_config
from fastapi_demo.manager.websocket_manager import websocket_manager
import logging
from fastapi_demo.rest_controllers import user_controller
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

logging.config.dictConfig(log_config.LOGGING_CONFIG)
log = logging.getLogger(__name__)

app = FastAPI()

# Mount the static directory to serve CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define the directory where HTML templates are stored
templates = Jinja2Templates(directory="templates")

app.include_router(user_controller.router)

# Configure CORS to allow your frontend local development server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite's default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# WebSocket endpoint start
@app.websocket("/connect")
async def websocket_endpoint(websocket: WebSocket):
    log.info(f'WebSocket endpoint called: {websocket}')
    await websocket_manager.connect(websocket)
    try:
        while True:
            # Wait for data from the client
            data = await websocket.receive_text()
            # Broadcast it out to all active clients
            await websocket_manager.broadcast(data)
    except WebSocketDisconnect:
        log.error(f'WebSocket endpoint disconnected: {websocket}')
        websocket_manager.disconnect(websocket)

# WebSocket endpoint end

#Global exception handler
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    log.error(f'Error while processing request body {exc.body} \n error details {exc.errors()}')
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": exc.errors(), "body": exc.body},
    )

#if you don't use response_class=HTMLResponse then it will consider it as application/json
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    log.info("Home page is loaded.")
    context = {
        "title": "Test Title",
    }
    return templates.TemplateResponse(
        request=request, name="index.html", context=context
    )

@app.get("/signup", response_class=HTMLResponse)
async def get_signup(request: Request):
    return templates.TemplateResponse(request=request, name="signup.html", context={})