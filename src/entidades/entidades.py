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
    
class Planta(SerVivo):
    def __init__(self , posicao_obj:Posicao , tamanho:float = 0.0):
        super().__init__(posicao_obj)
        self.tamanho = tamanho
    
    def crescer(self) -> None:
        if self.vivo:
            self.tamanho = round(self.tamanho + 0.2, 1)  # round evita dízimas do float
        
    def envelhecer(self) -> None:
        super().envelhecer() # Roda envelhecer de Servivo
        self.crescer() #Roda crescer
        
    def __str__(self) -> str:
        
        return (
            f"{super().__str__()} " 
            f"- tamanho: {self.tamanho}"     
            )
    
    
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
    def __init__(self , posicao_obj:Posicao  ,):
        super().__init__(posicao_obj , const.ENERGIA_COELHO , const.PERCEPCAO_COELHO)
        
    def __str__(self) -> str:
        return f"{super().__str__()}"
        
        