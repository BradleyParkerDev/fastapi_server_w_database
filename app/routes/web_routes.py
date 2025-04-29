from fastapi import APIRouter, Request, Response
from app.controllers.web import auth_page_controller, home_page_controller, user_page_controller

class WebRoutes():

    # Class constructor
    def __init__(self):
        self.router = APIRouter()

    # Individual Routes
    def setup_routes(self):
        @self.router.get("/")
        async def home_page_route(request:Request, response:Response):
            return await home_page_controller(request, response)
        @self.router.get("/auth")
        async def auth_page_route(request:Request, response:Response):
            return await auth_page_controller(request, response)
        @self.router.get("/user/{id}")
        async def user_page_route(request:Request, response:Response, id:str):
            return await user_page_controller(request, response, id=id)
        return self.router
    
