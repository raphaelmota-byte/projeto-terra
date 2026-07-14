from mundo.posicao import Posicao
import config.constantes as const

class Entidade:
    def __init__(self , posicao_obj:Posicao ):
        self.posicao = posicao_obj
    
    
    def __repr__(self):
        return f"{self.__class__.__name__}(posicao=({self.posicao.x},{self.posicao.y})"
       
        

class SerVivo(Entidade):
    def __init__(self , posicao_obj:Posicao):
        super().__init__(posicao_obj)
        self.idade:int = 0
        self.vivo:bool = True
        
    def envelhecer(self) -> None:
        self.idade += 1
    
    def morrer(self):
        self.vivo = False
        
    def __str__(self) -> str:
        return ( 
            f"Ser: {self.__class__.__name__} "
            f"Idade: {self.idade} "
            f"Vivo: {self.vivo} "
            f"Posição:{self.posicao}" 
            )
    
    def __repr__(self) -> str:
        return super().__repr__()
    
    

   