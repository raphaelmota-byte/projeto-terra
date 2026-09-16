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
        
    def to_dict(self):
        return{
            "posicao" : self.posicao.to_dict() ,
            "tipo" : self.tipo ,
            "entidades_celula" : [entidade.to_dict() for entidade in self.entidades]
        }
        
    def __repr__(self) :
        if self.entidades:
            ultima_entidade = self.entidades[-1]
            return ultima_entidade.icone
            
        
        elif self.tipo == "terra":
            return "🟩"
        elif self.tipo == "agua":
            return "🟦"
        
        
class Mapa:
    def __init__(self , largura:int , comprimento:int ) -> None :
        self.largura = largura
        self.comprimento = comprimento
        self.celulas = self.gerar_celulas() #grid principal
        self.gerar_agua()
        
    def validar_posicao(self , posicao:Posicao):
        #uso de raise para quebrar logo o código e evitar bugs invisíveis , que só podem acontecer por error de código e não pelo comportamento dos animais, no futuro.
        
        posicao_valida_x = (posicao.x < self.largura and posicao.x >= 0 ) 
        posicao_valida_y = (posicao.y < self.comprimento and posicao.y >= 0 ) 
        
        if not(posicao_valida_x) or not(posicao_valida_y) : 
            raise IndexError(f"a posição X: {posicao.x} deveria ser 0 < pos_x < {self.largura} e a posição Y 0 < pos_y < {self.comprimento} ") 
        return True
    
    def gerar_celulas(self):
       return [ [Celula(Posicao(x , y)) for x in range(self.largura)] for y in range(self.comprimento) ]
   
    def obter_celula(self , posicao:Posicao):
        if self.validar_posicao(posicao):
            return self.celulas[posicao.y][posicao.x] # y corresponde a altura (igual o i) e o x funciona como o j
   
    def gerar_agua(self):
        for linha in self.celulas:
            for celula in linha:
                if random.random() < const.CHANCE_AGUA: # TODO:adicionar seed fixa para tornar a geração de água determinística
                    celula.transformar_em_agua()
                    
    def adicionar_entidade(self , entidade:Entidade):
        celula = self.obter_celula(entidade.posicao)
        celula.adicionar(entidade)
    
    
    def remover_entidade(self , entidade:Entidade):
        celula = self.obter_celula(entidade.posicao)
        celula.remover(entidade)
       
        
    def __str__(self): #como o mapa (hoje) são quadradinhos esse é melhor jeito de imprimi-los 
        mapa_texto = ""

        for linha in self.celulas:
            for celula in linha:
                mapa_texto += str(celula) + " "
            
            mapa_texto += "\n"

        return mapa_texto
    
    
   
   
    
