from fastapi import FastAPI

app = FastAPI()


@app.get("/")
@app.get('/index.html')
async def root():
    return {"message": "Welcome to Theorems as a Service"}

@app.get("/theorem")
async def root():
    return {"message": "Pythagorean Theorem: There exist three numbers a b and c, not all the same, such that a^2 + b^2 = c^2 "}