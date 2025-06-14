from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from backend.routes.api_router import router

# Create the FastAPI app
app = FastAPI()

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include API router for backend routes
app.include_router(router)

# Set path for frontend static files
frontend_path = Path(__file__).resolve().parent.parent / "frontend"

# Serve static files (CSS, JS, images, etc.) from the 'frontend' directory
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

# Define a route to serve the index.html file
@app.get("/", response_class=HTMLResponse)
async def serve_index():
    # Serve the 'index.html' file from the frontend folder
    index_file = frontend_path / "index.html"
    return index_file.read_text(encoding="utf-8")

# Run the app with uvicorn for development purposes
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
