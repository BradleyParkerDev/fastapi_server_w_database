from fastapi import APIRouter, Request, Response
from app.controllers.user import  register_user_controller, get_user_controller, update_user_controller, delete_user_controller

class UserRoutes:
    def __init__(self):
        self.router = APIRouter()

    def setup_routes(self):

        # Register User
        @self.router.post("/api/user/register-user")
        async def register_user_route(request: Request, response: Response):
            return await register_user_controller(request, response)

        # Get User
        @self.router.get("/api/user/get-user")
        async def get_user_route(request: Request, response: Response):
            return await get_user_controller(request, response)

        # Update User
        @self.router.put("/api/user/update-user")
        async def update_user_route(request: Request, response: Response):
            return await update_user_controller(request, response)

        # Delete User
        @self.router.delete("/api/user/delete-user")
        async def delete_user_route(request: Request, response: Response):
            return await delete_user_controller(request, response)

        return self.router     
