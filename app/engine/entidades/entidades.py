from app.engine.mundo.posicao import Posicao
import app.engine.config.constantes as const
from typing import Any

class Entidade:
    def __init__(self , posicao_obj:Posicao ):
        self.posicao = posicao_obj
    
    def to_dict(self):
        return {"posicao_entidade" : self.posicao.to_dict()}
    
    def __repr__(self):
        return f"{self.__class__.__name__}(posicao=({self.posicao.x},{self.posicao.y})"
       
        

class SerVivo(Entidade):
    def __init__(self , posicao_obj:Posicao):
        super().__init__(posicao_obj)
        self.horas:int = 0
        self.vivo:bool = True
        
    def mostrar_idade(self):
        dias =  (self.horas//24)
        meses = (dias//30)
        anos =  (meses//12)
        
        return f"{self.horas % 24} horas | {dias % 30} dias | { meses % 12} meses| {anos} anos"
        
        
    def envelhecer(self) -> None:
        self.horas += 3
       
    
    def morrer(self):
        self.vivo = False
    
    def estar_vivo(self):
        return self.vivo
    
    def reproduzir(self):
            #vazio para ser rescrita pelos filhos
        return None
        
    def atualizar(self):
        self.envelhecer()
        
    def __str__(self) -> str:
        return ( 
            f"Espécie:{self.__class__.__name__} | "
            f"Tempo de vida: {self.mostrar_idade()} | "
            f"Vivo:{self.vivo} | "
            f"Posição:{self.posicao}" 
            )
    
    def __repr__(self) -> str:
        return super().__repr__()
    
    def to_dict(self):
        dados: dict[str , Any] = super().to_dict()
        
        dados.update({
            "vivo" : self.vivo ,
            "horas_vida" : self.horas ,
            "idade_formatada" : self.mostrar_idade()
        })
        
        return dados
    
    

   