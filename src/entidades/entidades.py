from mundo.posicao import Posicao



class Entidade:
    def __init__(self , posicao_obj:Posicao ):
        self.posicao_coordenada:tuple[int , int] = posicao_obj.posicao
       
        

class SerVivo(Entidade):
    def __init__(self , posicao_obj:Posicao):
        super().__init__(posicao_obj )
        self.idade:int = 0
        self.vivo:bool = True
        
    def envelhecer(self) -> None:
        self.idade += 1
    
    def morrer(self):
        self.vivo = False
        
    def __str__(self) -> str:
        return f"idade do ser {self.idade} - ele está vivo?: {self.vivo} - posição:{self.posicao_coordenada}"
    
    
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
        return f"{super().__str__()} - tamanho: {self.tamanho}"