from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from theorem_generator import random_theorem


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
@app.get('/index.html', response_class=HTMLResponse)
async def theorem_html():
    theorem = random_theorem()
    content = f"""
    <html>
        <head>
            <title>Theorems as a Service</title>
            <link id="favicon" rel="icon" type="image/x-icon" href="static/favicon.ico">
            <script defer src="https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-chtml.js"></script>
            <script>
                MathJax = {{
                tex: {{
                    inlineMath: {{'[+]': [['$', '$']]}}
                }}
                }};
            </script>
            <script defer src="https://cdn.jsdelivr.net/npm/mathjax@4/tex-chtml.js"></script>
        </head>
        <body>
            <h1 style="font-family: Arial;">Welcome to Theorems as a Service!</h1>
            <div style="font-family: Arial;">
                <p>Here's a math theorem for you:</p>
            </div>
            <div style="font-family: Arial;">
                <p>{theorem}</p>
            </div>
            <div style="font-family: Arial;">
               <button onClick="window.location.reload();">Refresh Page For Another Theorem</button>
            </div>
        </body>
    </html>
    """
    return content
    
@app.get("/theorem")
async def theorem_api():
    theorem = random_theorem()
    return {"theorem": f"{theorem}"}