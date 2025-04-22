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


async def home_page_controller(request:Request, response:Response):

    greeting = "Hello, World!!! \n This is a FastAPI Server with a Database!!!"

    return templates.TemplateResponse("pages/home_page.html",{
        "request": request,  # Pass the request object
        "greeting": greeting,
        "DEBUG": DEBUG,
        "hotreload": layout.arel.hotreload
    }) 