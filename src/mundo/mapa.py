import random
import config.constantes as const 
from mundo.posicao import Posicao


class Celula:
    def __init__(self  , posicao:Posicao ,tipo="terra"):
        self.posicao_obj = posicao
        self.posicao_coordenadas = posicao.posicao
        self.tipo = tipo
        self.entidades = []
        
    def transformar_em_agua(self):
        self.tipo = "agua"
        
 
        
    def __repr__(self) :
        if self.tipo == "terra":
            return "🟩"
        elif self.tipo == "agua":
            return "🟦"
        
        
class Mapa:
    def __init__(self , largura:int , comprimento:int ) -> None :
        self.largura = largura
        self.comprimento = comprimento
        self.celulas = self.gerar_celulas()
        
        
    def gerar_celulas(self):
       return [ [Celula(Posicao(x , y)) for x in range(self.largura)] for y in range(self.comprimento) ]
   
    def gerar_agua(self):
        for linha in self.celulas:
            for celula in linha:
                if random.random() < const.CHANCE_AGUA:
                   celula.transformar_em_agua()
       
        
    def __str__(self):
        return f"largura: {self.largura} , comprimento: {self.comprimento} "
   
   
    
