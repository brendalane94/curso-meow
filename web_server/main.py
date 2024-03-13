import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def get_list():
    return [1, 2, 3]

@app.get("/contact", response_class=HTMLResponse)
def get_contact():
    return """
    <h1 style="color:purple; text-align:center"> HOLIX MIAUSIS </h1>
    <p> "Mata su luz un fuego abandonado.
Sube su canto un pájaro enamorado.
Tantas criaturas ávidas en mi silencio
y esta pequeña lluvia que me acompaña"</p>
    <p> Alejandra Pizarnik </p>
    """
def run():
    store.get_categories()

if __name__ == '__main__':
    run()