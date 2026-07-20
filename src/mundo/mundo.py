from mundo.mapa import Mapa
from entidades.entidades import Entidade

class Mundo:
    def __init__(self , mapa_obj:Mapa) -> None:
        self.mapa = mapa_obj # o mundo contem o mapa
        self.entidades_mundo = []
        
    def adicionar_entidade(self , entidade:Entidade):
        self.entidades_mundo.append(entidade)
        self.mapa.adicionar_entidade(entidade)
        
    def remover_entidade(self , entidade:Entidade):
        if entidade in self.entidades_mundo:
            self.entidades_mundo.remove(entidade) # o remove serve pra remover pelo valor
            self.mapa.remover_entidade(entidade)
    
    def remover_mortos(self):
        entidades = self.entidades_mundo.copy()
        
        for entidade in entidades:
            if not entidade.estar_vivo():
                self.remover_entidade(entidade)
    
    def atualizar(self):
        entidades = self.entidades_mundo.copy()
        
        for entidade in entidades:
            entidade.atualizar()
        self.remover_mortos()
        
    def __str__(self):
        return f"o mundo possui {len(self.entidades_mundo)} entidades"