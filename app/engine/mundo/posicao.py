
class Posicao:
    def __init__(self , posicao_x:int , posicao_y:int) -> None:
        self.x = posicao_x  
        self.y = posicao_y
    def __str__(self):
        return f"({self.x},{self.y})"