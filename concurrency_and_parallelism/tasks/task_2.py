"""
This web application built on top-of asyncio shows inconsistent response times for /health endpoint.

Normally, when there is no load, the endpoint responds in a fraction of the second.
However, when at the same time users register or login, the health endpoint responds dramatically slower - over 1s.

To test:
1. Run this file as script and keep it running
    uv run python concurrency_and_parallelism/tasks/task_2.py

2. Run verification script in another window
    uv run python concurrency_and_parallelism/tasks/task_2_verification.py

The verification script will first hit /health endpoint a few times, then will start using /register, /login and /health
endpoints simultaneously. You should observe a slowdown for /health endpoint.

The issue is that cryptographic operations during /login and /register are CPU-heavy and will block asyncio event loop.

To circumvent this idea, create an instance of appropriate Executor (Threads, Subinterpreters or Processes) and use it
at least in /users/login endpoint function.
"""
import asyncio
import os

import uvicorn
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.exceptions import InvalidKey
from fastapi import FastAPI, Response
from pydantic import BaseModel


salt = os.urandom(16)

def get_kdf() -> Scrypt:
    return Scrypt(
        salt=salt,
        length=128,
        n=2**16,
        r=12,
        p=3,
    )

_users: dict[str, bytes] = {}

app = FastAPI()


@app.get("/health")
async def health() -> Response:
    return Response(status_code=204)


class CredentialsPayload(BaseModel):
    username: str
    password: str


@app.post("/users/register")
async def register(credentials: CredentialsPayload) -> Response:
    if credentials.username in _users:
        return Response(status_code=400)
    else:
        kdf = get_kdf()
        password_as_bytes = credentials.password.encode()
        encrypted_password = kdf.derive(password_as_bytes)  # this blocks
        _users[credentials.username] = encrypted_password
        return Response(status_code=201)


@app.post("/users/login")
async def login(credentials: CredentialsPayload) -> Response:
    if credentials.username not in _users:
        return Response(status_code=403)
    encrypted_password = _users[credentials.username]
    given_password_bytes = credentials.password.encode()
    kdf = get_kdf()
    try:
        # loop = asyncio.get_running_loop()
        # await loop.run_in_executor()
        kdf.verify(given_password_bytes, encrypted_password)  # this blocks
    except InvalidKey:
        return Response(status_code=403)
    return Response(status_code=200)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
