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


async def home_page_controller(request:Request, response:Response):

    logger = get_logger("web")
    logger.info("User accessed home page!!!")
    
    greeting = "Hello, World!!! \n This is a FastAPI server with a database!!!"

    return templates.TemplateResponse("pages/home_page.html",{
        "request": request,  # Pass the request object
        "greeting": greeting,
        "DEBUG": DEBUG,
        "hotreload": layout.arel.hotreload
    }) 