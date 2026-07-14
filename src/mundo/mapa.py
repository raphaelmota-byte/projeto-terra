import random


class Celula:
    def __init__(self  , pos_x , pos_y ,tipo="terra"):
        self.x = pos_x
        self.y = pos_y
        self.tipo = tipo
        
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
       return [ [Celula(x , y) for x in range(self.largura)] for y in range(self.comprimento) ]
   
    def gerar_agua(self):
        pass
       
        
    def __str__(self):
        return f"largura: {self.largura} , comprimento: {self.comprimento} "
   
   
    

mapa = Mapa(16 , 16 )
print(mapa)
for linhas in mapa.celulas:
    print(*linhas)