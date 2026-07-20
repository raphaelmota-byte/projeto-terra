from entidades.entidades import SerVivo
from mundo.posicao import Posicao
import config.constantes as const
 
class Animal(SerVivo):
    CONSUMO_ENERGIA = 0
    ENERGIA_INICIAL = 0
    PERCEPCAO = 0
    
    def __init__(self, posicao_obj:Posicao ):
        super().__init__(posicao_obj)
        self.energia = self.ENERGIA_INICIAL

    def gastar_energia(self):
        self.energia -= self.CONSUMO_ENERGIA
        if self.energia <= 0:
            self.morrer()
    
    def alimentar(self):
        pass

    def reproduzir(self):
        pass
    
    def atualizar(self):
        super().atualizar()
        self.gastar_energia()


class Coelho(Animal):
    PERCEPCAO = const.PERCEPCAO_COELHO
    ENERGIA_INICIAL = const.ENERGIA_INICIAL_COELHO
    CONSUMO_ENERGIA = const.CONSUMO_ENERGIA_COELHO
    
   
        
    def __str__(self) -> str:
        return f"{super().__str__()}"
    
class Cobra(Animal):
    PERCEPCAO = const.PERCEPCAO_COBRA
    ENERGIA_INICIAL = const.ENERGIA_INICIAL_COBRA
    CONSUMO_ENERGIA = const.CONSUMO_ENERGIA_COBRA
    
  
        
    def __str__(self) -> str:
        return f"{super().__str__()}"
        
        
class Gaviao(Animal):
    PERCEPCAO = const.PERCEPCAO_GAVIAO
    ENERGIA_INICIAL = const.ENERGIA_INICIAL_GAVIAO
    CONSUMO_ENERGIA = const.CONSUMO_ENERGIA_GAVIAO
    
    def __str__(self) -> str:
        return super().__str__()