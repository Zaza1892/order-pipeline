from fastapi import FastAPI
import hashlib
import random


app=FastAPI()

@app.get("/health")

def health():
    return {"status":"ok"}

@app.get("/lookup/{order_id}")
def lookup(order_id:str):
    order_seed = int(hashlib.sha256(order_id.encode()).hexdigest(),16) %(10 ** 8)
    order_generator=random.Random(order_seed)