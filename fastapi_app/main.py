from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi_demo.config import log_config
import logging
from fastapi_demo.rest_controllers import user_controller

logging.config.dictConfig(log_config.LOGGING_CONFIG)
log = logging.getLogger(__name__)

app = FastAPI()
app.include_router(user_controller.router)

#Global exception handler
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    log.error(f'Error while processing request body {exc.body} \n error details {exc.errors()}')
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": exc.errors(), "body": exc.body},
    )

@app.get("/")
async def home():
    log.info("Home page is loaded.")
    return {"message": "Application is running."}