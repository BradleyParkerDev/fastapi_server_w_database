import json
from app.lib.logger import get_logger
from fastapi import Request, Response, HTTPException, status

# delete user controller
async def delete_user_controller(request:Request, response:Response):
    logger = get_logger("user")
    logger.info("User successefully deleted!!!")
    return {"message": "User successefully deleted!!!"}
