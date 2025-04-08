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


async def user_page_controller(request:Request, response:Response):

    heading = "This is a user page!!!"
    message = "This will be used to login/register."

    return templates.TemplateResponse("pages/user_page.html",{
        "request": request,  # Pass the request object
        "heading": heading,
        "message": message,
        "DEBUG": DEBUG,
        "hotreload": layout.arel.hotreload
    }) 