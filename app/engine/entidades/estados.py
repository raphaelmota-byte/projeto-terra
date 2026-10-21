from abc import ABC , abstractmethod
from ..config import constantes as const

#a classe abstrata é o molde e reclama de error se as filhas não rescreverem seus métodos
class EstadoAnimal(ABC):
    
    @abstractmethod
    def processar_fome(self , animal , vizinhos): 
        pass
    
    @abstractmethod
    def processar_reproducao(self, animal, vizinhos):
        pass

class Satisfeito(EstadoAnimal):
    def processar_fome(self , animal , vizinhos):
        if animal.energia <= (animal.ENERGIA_INICIAL * const.ENTRAR_ESTADO_FAMINTO):
            # print(f"{animal.__class__.__name__} tem {animal.energia} de energia e ficou com fome!")
            animal.estado = Faminto()
        return None
    
    def processar_reproducao(self, animal, vizinhos):
        filhote = animal.executar_reproducao(vizinhos)
        
        # if filhote:
        #     print(f"Filhote de {animal.__class__.__name__} nasceu!!")
            
        # Devolvemos o filhote para a classe Mundo adicioná-lo ao mapa
        return filhote
    
class Faminto(EstadoAnimal):
    def processar_fome(self, animal, vizinhos):
        animal.executar_alimentacao(vizinhos)
        
        if animal.energia >= (animal.ENERGIA_INICIAL * const.ENTRAR_ESTADO_SATISFEITO):
            # print(f"{animal.__class__.__name__} tem {animal.energia} de energia ficou cheio/satisfeito!")
            animal.estado = Satisfeito()
    
    
    def processar_reproducao(self, animal, vizinhos):
        return None