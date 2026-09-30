from fastapi import FastAPI
from app.engine.mundo.posicao import Posicao
from app.engine.entidades.animais import Coelho, Cobra, Gaviao
from app.engine.mundo.mundo import Mundo
from app.engine.mundo.mapa import Mapa
from app.schemas import AvancaTick

app = FastAPI()

# Variável global que mantém a instância de Mundo viva na memória do servidor
simulacao_atual = None

@app.post("/iniciar")
def iniciar_mundo():
    global simulacao_atual
    
    # Instancia Mundo(largura, altura) e sobrescreve a variavel simulacao_atual
    # O tamanho inicial do mundo planejado é 16 × 16[cite: 4]
    tamanho_mapa = 16
    mapa = Mapa(tamanho_mapa, tamanho_mapa)
    simulacao_atual = Mundo(mapa)
    
    # Vamos adicionar um coelho para teste inicial
    pos = Posicao(1, 1)
    coelho = Coelho(pos)
    simulacao_atual.adicionar_entidade(coelho)
    
    return {"mensagem": "Mundo iniciado com sucesso"}

@app.post("/tick")
def atualizar_mundo(dados: AvancaTick):
    global simulacao_atual
    
    if simulacao_atual is None:
        return {"erro": "Inicie o mundo primeiro chamando a rota /iniciar"}
        
    for i in range(dados.tick):
        # Chama simulacao_atual.atualizar() para processar 1 turno de tempo[cite: 3]
        simulacao_atual.atualizar()
        
    return {"mensagem": f"Mundo atualizado em {dados.tick} ticks com sucesso"}

@app.get("/estado")
def obter_estado():
    global simulacao_atual
    
    if simulacao_atual is None:
        return {"erro": "Inicie o mundo primeiro chamando a rota /iniciar"}
        
    # Chama simulacao_atual.to_dict() e o FastAPI automaticamente traduz o dicionário resultante para um arquivo JSON entregue ao front-end[cite: 3]
    return simulacao_atual.to_dict()