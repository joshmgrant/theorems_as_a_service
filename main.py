from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from theorem_generator import random_theorem


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
@app.get('/index.html', response_class=HTMLResponse)
async def theorem_html():
    theorem = random_theorem()
    content = f"""
    <html>
        <head>
            <title>Theorems as a Service</title>
        </head>
        <body>
            <h1>Welcome to Theorems as a Service!</h1>
            <div>
                <p>Here's a math theorem for you:</p>
            </div>
            <div>
                <p>{theorem}</p>
            </div>
        </body>
    </html>
    """
    return content
    
@app.get("/theorem")
async def theorem_api():
    theorem = random_theorem()
    return {"theorem": f"{theorem}"}