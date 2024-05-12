import uvicorn
from fastapi import FastAPI, Response, Path, Query, Body, Header
from fastapi.responses import HTMLResponse, PlainTextResponse, JSONResponse, FileResponse
import database
from public.router_users import users_router,classes_router

app = FastAPI(
    title="My FastAPI Application",
    description="This is a very fancy project, with auto docs for the API and everything",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json",
    docs_url="/docs",
    redoc_url=None
)

app.include_router(users_router)
app.include_router(classes_router)


@app.get("/")
def main():
    return FileResponse("files/index.html")


if __name__ == "__main__":
   uvicorn.run(app,host="127.0.0.1", port=8000)