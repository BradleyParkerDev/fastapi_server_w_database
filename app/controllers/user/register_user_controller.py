import json
from app.database.models import User
from app.lib.logger import get_logger
from fastapi import Request, Response, HTTPException, status

# register user controller
async def register_user_controller(request:Request, response:Response):
    logger = get_logger("user")
    logger.info("User successefully registered!!!")
    request_body = await request.json()
    print(request_body['first_name'])
    return {"message": "User successefully registered!!!"}
