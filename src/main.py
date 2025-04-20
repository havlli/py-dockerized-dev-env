from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import redis

app = FastAPI(
    title="FastAPI Template",
    description="A template for FastAPI applications",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

r = redis.Redis(host="redis", port=6379)

import debugpy
debugpy.listen(("0.0.0.0", 5678))

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Template!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/hits")
def read_item():
    r.incr("hits")
    return {"hits": r.get("hits")}