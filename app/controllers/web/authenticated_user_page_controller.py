import os
from dotenv import load_dotenv
from fastapi import Request, Response, HTTPException, status
from fastapi.templating import Jinja2Templates 
from app.lib import LayoutUtility

templates = Jinja2Templates(directory="resources/templates")

# Load environment variables
load_dotenv()
DEBUG = os.getenv("DEBUG")

# Layout utility
layout = LayoutUtility()


async def authenticated_user_page_controller(request:Request, response:Response, id:str):

    heading = "This is an authenticated user page!!!"
    message = (f"User Name:{id}")

    return templates.TemplateResponse("pages/authenticated_user_page.html",{
        "request": request,  # Pass the request object
        "heading": heading,
        "message": message,
        "DEBUG": DEBUG,
        "hotreload": layout.arel.hotreload
    }) 