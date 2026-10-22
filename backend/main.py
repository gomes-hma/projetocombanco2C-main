
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from rotas import clientes, senioridade, tatuadores, agendamentos, estilos
import os

app = FastAPI()

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cria a pasta de uploads caso não exista
os.makedirs("uploads", exist_ok=True)

# Disponibiliza as imagens enviadas
app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads"
)

# Registra as rotas da API
app.include_router(clientes.router)
app.include_router(senioridade.router)
app.include_router(tatuadores.router)
app.include_router(agendamentos.router)


# Rota inicial
@app.get("/")
def inicio():
    return {
        "mensagem": "API do estúdio de tatuagem funcionando!"
    }

    from rotas import clientes, senioridade, tatuadores, agendamentos, estilos   # ← adiciona estilos aqui
...
app.include_router(estilos.router)   # ← registra a nova rota
