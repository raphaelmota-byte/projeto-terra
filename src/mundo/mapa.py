import random
import config.constantes as const 
from mundo.posicao import Posicao
from entidades.entidades import Entidade


class Celula:
    def __init__(self  , posicao_obj:Posicao ,tipo="terra"):
        self.posicao = posicao_obj
        self.tipo = tipo
        self.entidades = []
        
    def adicionar(self , entidade):
        self.entidades.append(entidade)
    
    def remover(self , entidade):
        if entidade in self.entidades:
            self.entidades.remove(entidade)
        
        
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
        self.celulas = self.gerar_celulas() #grid principal
        self.gerar_agua()
        
        
    def gerar_celulas(self):
       return [ [Celula(Posicao(x , y)) for x in range(self.largura)] for y in range(self.comprimento) ]
   
    def obter_celula(self , posicao:Posicao):
        return self.celulas[posicao.x][posicao.y]
   
    def gerar_agua(self):
        for linha in self.celulas:
            for celula in linha:
                if random.random() < const.CHANCE_AGUA:
                   celula.transformar_em_agua()

    def adicionar_entidade(self , entidade:Entidade):
        celula = self.obter_celula(entidade.posicao)
        celula.adicionar(entidade)
    
    
    def remover_entidade(self , entidade:Entidade):
        celula = self.obter_celula(entidade.posicao)
        celula.remover(entidade)
       
        
    def __str__(self):
        mapa_texto = ""

        for linha in self.celulas:
            for celula in linha:
                mapa_texto += str(celula) + " "
            
            mapa_texto += "\n"

        return mapa_texto
    
    
   
   
    
