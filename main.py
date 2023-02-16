from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_html():
    TARGET_LANGUAGE = 'es'
    with open(f"website-A_translated_{TARGET_LANGUAGE}.html", "r", encoding='utf-8') as file:
        html_content = file.read()
    return html_content

