import json
from fastapi import Request, Response, HTTPException, status

# update user controller
async def update_user_controller(request:Request, response:Response):
    return {"message": "User data successefully updated!!!"}
