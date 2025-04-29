import os
from dotenv import load_dotenv
from app.lib.logger import get_logger
from fastapi import Request, Response, HTTPException, status
from fastapi.templating import Jinja2Templates 
from app.lib import LayoutUtility

templates = Jinja2Templates(directory="resources/templates")

# Load environment variables
load_dotenv()
DEBUG = os.getenv("DEBUG")

# Layout utility
layout = LayoutUtility()


async def auth_page_controller(request:Request, response:Response):

    logger = get_logger("web")
    logger.info("User accessed auth page!!!")
    
    heading = "This is an auth page!!!"
    message = "This will be used to login/register a user."

    return templates.TemplateResponse("pages/auth_page.html",{
        "request": request,  # Pass the request object
        "heading": heading,
        "message": message,
        "DEBUG": DEBUG,
        "hotreload": layout.arel.hotreload
    }) 