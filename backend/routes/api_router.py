from fastapi import APIRouter, Request
from backend.routes.actions import handle_action

router = APIRouter()

@router.post("/voice-command/")
async def process_command(request: Request):
    data = await request.json()
    command = data.get("command", "")
    response_text, html_response = await handle_action(command)
    return {"text": response_text, "html": html_response}

# ✅ Add this status route
@router.get("/status")
async def get_status():
    return {"status": "up"}
