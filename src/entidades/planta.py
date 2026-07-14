from entidades.entidades import SerVivo
from mundo.posicao import Posicao

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
    