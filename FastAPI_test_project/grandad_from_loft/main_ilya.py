from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.websockets import WebSocket, WebSocketDisconnect
from pathlib import Path
import asyncio
from database import get_db, DATABASE_URL
from open_router import agent

app = FastAPI()
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")

active_connections = []

@app.on_event("startup")
async def startup_event():
    app.state.db = await get_db(DATABASE_URL)

@app.on_event("shutdown")
async def shutdown_event():
    await app.state.db.close()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:

            data = await websocket.receive_json()
            async with app.state.db.acquire() as conn:
                await conn.execute(
                    "INSERT INTO messages (text, class) VALUES ($1, $2)",
                    data["text"], data["class"]
                )

            for connection in active_connections:
                await connection.send_json(data)

            agent_response = {"text": agent(data["text"]), "class": "agent"}
            async with app.state.db.acquire() as conn:
                await conn.execute(
                    "INSERT INTO messages (text, class) VALUES ($1, $2)",
                    agent_response["text"], agent_response["class"]
                )

            for connection in active_connections:
                await connection.send_json(agent_response)
    except WebSocketDisconnect:
        active_connections.remove(websocket)


@app.get("/", response_class=HTMLResponse)
async def read_chat(request: Request):
    async with app.state.db.acquire() as conn:
        rows = await conn.fetch("SELECT text, class FROM messages ORDER BY id DESC LIMIT 50")
    messages = [{"text": row["text"], "class": row["class"]} for row in reversed(rows)]
    return templates.TemplateResponse("chat.html", {"request": request, "messages": messages})

