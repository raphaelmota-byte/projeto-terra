from entidades.entidades import SerVivo
from mundo.posicao import Posicao
import config.constantes as const
 
class Animal(SerVivo):
    def __init__(self, posicao_obj:Posicao , energia , percepcao):
        super().__init__(posicao_obj)
        self.energia = energia
        self.percepcao = percepcao

    def gastar_energia(self):
        pass
    
    def alimentar(self):
        pass

    def reproduzir(self):
        pass


class Coelho(Animal):
    def __init__(self , posicao_obj:Posicao ):
        super().__init__(posicao_obj , const.ENERGIA_COELHO , const.PERCEPCAO_COELHO)
        
    def __str__(self) -> str:
        return f"{super().__str__()}"
    
class Cobra(Animal):
    def __init__(self, posicao_obj: Posicao):
        super().__init__(posicao_obj, const.ENERGIA_COBRA, const.PERCEPCAO_COBRA)
        
    def __str__(self) -> str:
        return f"{super().__str__()}"
        
        
class Gaviao(Animal):
    def __init__(self, posicao_obj: Posicao):
        super().__init__(posicao_obj, const.ENERGIA_GAVIAO, const.PERCEPCAO_GAVIAO)  
    
    def __str__(self) -> str:
        return super().__str__()