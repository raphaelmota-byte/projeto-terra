from fastapi import FastAPI
from .engine.mundo.posicao import Posicao
from .engine.entidades.entidades import Entidade , SerVivo
from .engine.entidades.animais import Coelho , Cobra , Gaviao
from .engine.mundo.mundo import Mundo
from .engine.mundo.mapa import Mapa

app = FastAPI()

@app.get("/teste_primeiras_classes")
def testar_objetos():
    pos = Posicao(3 , 7)
    entidade = Entidade(pos)
    ser_vivo = SerVivo(pos)
    return {
        "objeto Posiçao" : pos.to_dict() ,
        "entidade" : entidade.to_dict() ,
        "ser_vivo" : ser_vivo.to_dict()
            
            }
    
@app.get("/teste_animal")
def testar_animal():
    pos = Posicao(1 , 1)
    coelho = Coelho(pos)
    cobra = Cobra(pos)
    gaviao = Gaviao(pos)
    return{
        "coelho" : coelho.to_dict() ,
        "cobra" : cobra.to_dict() ,
        "gaviao" : gaviao.to_dict()
    }
    
@app.get("/teste_mapa")
def teste_mapa():
    tamanho_mapa = 2

    mapa = Mapa(tamanho_mapa , tamanho_mapa )
    mundo = Mundo(mapa)
    
    pos = Posicao(1 , 1)
    coelho = Coelho(pos)
    
    mundo.adicionar_entidade(coelho)
    celula = mapa.obter_celula(pos)
    
    return{
        "mundo" : mundo.to_dict()
    }
