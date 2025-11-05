from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
@app.get('/index.html', response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>Theorems as a Service</title>
        </head>
        <body>
            <h1>Welcome to Theorems as a Service!</h1>
            <div>Here's a math theorem for you:</div>
        </body>
    </html>
    """
@app.get("/theorem")
async def root():
    return {"theorem": "Pythagorean Theorem: There exist three numbers a b and c, not all the same, such that a^2 + b^2 = c^2 "}