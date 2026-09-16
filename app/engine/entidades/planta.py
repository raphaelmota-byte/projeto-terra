from entidades.entidades import SerVivo
from mundo.posicao import Posicao

class Planta(SerVivo):
    def __init__(self , posicao_obj:Posicao , tamanho:float = 0.0):
        super().__init__(posicao_obj)
        self.tamanho = tamanho
        self.icone = "🌲"
    
    def crescer(self) -> None:
        if self.vivo:
            self.tamanho = round(self.tamanho + 0.2, 1)  # round evita dízimas do float
        
    
    def atualizar(self):
        super().atualizar()
        self.crescer()
    
    def __str__(self) -> str:
        
        return (
            f"{super().__str__()} " 
            f"- tamanho: {self.tamanho}"     
            )
    