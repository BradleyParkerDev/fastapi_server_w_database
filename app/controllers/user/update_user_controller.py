import json
from app.lib.logger import get_logger
from fastapi import Request, Response, HTTPException, status

# update user controller
async def update_user_controller(request:Request, response:Response):
    logger = get_logger("user")
    logger.info("User successefully updated!!!")
    return {"message": "User data successefully updated!!!"}
