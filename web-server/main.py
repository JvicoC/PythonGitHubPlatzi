import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
#$ uvicorn main:app --reload
#CODIGO PARA HACER LA PRUEBA ESTE MAIN EN SHELL

app= FastAPI()

@app.get('/') #decorador ruta desde la web
def get_list():
    return [1,2,3]

@app.get('/usuarios',response_class=HTMLResponse)
def get_list():
    return """
        <h1>"HOLA MUNDO"</h1>
        <h2>soy vico vICOLAS</h2>        
    """
#def run():
 #   store.get_categories()

#if __name__=='__main__':
 #   run()