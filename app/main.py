from fastapi import FastAPI , HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.engine.mundo.posicao import Posicao
from app.engine.entidades.animais import Coelho, Cobra, Gaviao
from app.engine.entidades.planta import Planta
from app.engine.mundo.mundo import Mundo
from app.engine.mundo.mapa import Mapa
from app.schemas import AvancaTick , IniciarMundo
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permite requisições de qualquer porta (como a 5173 do Vite)
    allow_credentials=True,
    allow_methods=["*"], # Permite todos os métodos (GET, POST, OPTIONS, etc)
    allow_headers=["*"],
)

# Variável global que mantém a instância de Mundo viva na memória do servidor
simulacao_atual = None

@app.post("/iniciar")
def iniciar_mundo(dados:IniciarMundo):
    global simulacao_atual
    
    # Instancia Mundo(largura, altura) e sobrescreve a variavel simulacao_atual
    # O tamanho inicial do mundo planejado é 16 × 16
    tamanho_mapa = dados.tamanho_mapa
    
    mapa = Mapa(tamanho_mapa, tamanho_mapa)
    simulacao_atual = Mundo(mapa)
    limite = tamanho_mapa - 1
    
    # Adicionando os coelhos
    for _ in range(11):
        cord_x = random.randint(0, limite)
        cord_y = random.randint(0, limite)
        simulacao_atual.adicionar_entidade(Coelho(Posicao(cord_x, cord_y)))

    # Criando as Cobras 
    for _ in range(9):
        cord_x = random.randint(0, limite)
        cord_y = random.randint(0, limite)
        simulacao_atual.adicionar_entidade(Cobra(Posicao(cord_x, cord_y)))

    # Criando os Gaviões
    for _ in range(5):
        cord_x = random.randint(0, limite)
        cord_y = random.randint(0, limite)
        simulacao_atual.adicionar_entidade(Gaviao(Posicao(cord_x, cord_y)))
    
    for _ in range(10):
        cord_x = random.randint(0, limite)
        cord_y = random.randint(0, limite)
        simulacao_atual.adicionar_entidade(Planta(Posicao(cord_x, cord_y)))
        
    return {"mensagem": "Mundo iniciado com sucesso"}

@app.post("/tick")
def atualizar_mundo(dados: AvancaTick):
    global simulacao_atual
    
    if simulacao_atual is None:
        raise HTTPException(
                    status_code=404 , 
                    detail= "Inicie o mundo primeiro chamando a rota /iniciar"
                    )
        
    for _ in range(dados.tick):
        simulacao_atual.atualizar()
        
    return {"mensagem": f"Mundo atualizado em {dados.tick} ticks com sucesso"}

@app.get("/estado")
def obter_estado():
    global simulacao_atual
    
    if simulacao_atual is None:
        raise HTTPException(
            status_code=404 , 
            detail= "Inicie o mundo primeiro chamando a rota /iniciar"
            )
        
    return simulacao_atual.to_dict()
    
    
