import json
from fastapi import Request, Response, HTTPException, status

# delete user controller
async def delete_user_controller(request:Request, response:Response):
    return {"message": "User successefully deleted!!!"}
