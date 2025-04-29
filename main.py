import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.cors import CORSMiddleware  
from app.routes import WebRoutes, UserRoutes
from app.lib import AuthUtility, CronJobUtility, LayoutUtility
from starlette.routing import WebSocketRoute
import uvicorn


# Load environment variables
load_dotenv()
FASTAPI_PORT = int(os.getenv("FASTAPI_PORT", 3012))
DEBUG = os.getenv("DEBUG", "false").lower() == "true"


# Utilities
auth = AuthUtility()
layout = LayoutUtility()


# Create FastAPI App - Parameters for OpenAPI and Arel
app = FastAPI(title=os.getenv("APP_NAME"),
              docs_url=None if os.getenv("DEBUG") == "false" else "/docs",
              redoc_url=None if os.getenv("DEBUG") == "false" else "/redoc",
              openapi_url=None if os.getenv("DEBUG") == "false" else "/openapi.json",
              lifespan=layout.arel.lifespan) # Lifespan handler is attached to FastAPI


# Routes
user_routes = UserRoutes()
app.include_router(user_routes.setup_routes())

web_routes = WebRoutes()
app.include_router(web_routes.setup_routes())


# Middleware
app.add_middleware(GZipMiddleware) # For file compression

@app.middleware("http") # Authorization middleware
async def authorization_middleware(request:Request, call_next):
    response:Response = await auth.authorize_user(request, call_next)
    return response

@app.middleware("http") # No caching in the browser
async def no_cache_middleware(request:Request, call_next):
    response:Response = await call_next(request)
    response.headers["Cache_Control"] = "no-store"
    return response

app.add_middleware( # CORS Middleware - currently allows everything
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to restrict allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Adjust this to restrict allowed HTTP methods
    allow_headers=["*"],  # Adjust this to restrict allowed headers
)


# Mount static files in public directory
app.mount("/public", StaticFiles(directory="public"), name="public")


# Hot reloading websocket
app.router.routes.append(WebSocketRoute("/hot-reload", layout.arel.hotreload, name="hot-reload"))


# Start Server
if __name__ == "__main__":
    # uvicorn main:app --host 127.0.0.1 --port 4001 --reload
    uvicorn.run("main:app", host="127.0.0.1", port=FASTAPI_PORT, reload=DEBUG)






