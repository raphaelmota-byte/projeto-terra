from abc import ABC , abstractmethod
import random
from ..mundo.posicao import Posicao
from ..config import constantes as const

#a classe abstrata é o molde e reclama de error se as filhas não rescreverem seus métodos
class EstadoAnimal(ABC):
    
    @abstractmethod
    def processar_fome(self , animal , vizinhos): 
        pass
    
    @abstractmethod
    def processar_reproducao(self, animal, vizinhos):
        pass
    
    @abstractmethod
    def processar_movimento(self , animal):
        pass
    
    @abstractmethod
    def gastar_energia(self , animal):
        animal.energia -= animal.consumo_energia
        if animal.energia <= 0:
            animal.morrer()

class Satisfeito(EstadoAnimal):
    def processar_fome(self , animal , vizinhos):
        if animal.energia <= (animal.ENERGIA_INICIAL * const.ENTRAR_ESTADO_FAMINTO):
            # print(f"{animal.__class__.__name__} tem {animal.energia} de energia e ficou com fome!")
            animal.estado = Faminto()
        elif animal.energia >= (animal.ENERGIA_INICIAL * const.ENTRAR_ESTADO_DESCANSO):
            animal.estado = Descansando()
        return None
    
    def processar_reproducao(self, animal, vizinhos):
        filhote = animal.executar_reproducao(vizinhos)
        return filhote
    
    def processar_movimento(self, animal):
        movimentos = [(0,1) , (0,-1)  , (1,0)  , (-1,0)]
        dx , dy = random.choice(movimentos)
        return Posicao(animal.posicao.x + dx, animal.posicao.y + dy)
    
    def gastar_energia(self, animal):
        return super().gastar_energia(animal)
    
class Faminto(EstadoAnimal):
    def processar_fome(self, animal, vizinhos):
        animal.executar_alimentacao(vizinhos)
        
        if animal.energia >= (animal.ENERGIA_INICIAL * const.ENTRAR_ESTADO_SATISFEITO):
            # print(f"{animal.__class__.__name__} tem {animal.energia} de energia ficou cheio/satisfeito!")
            animal.estado = Satisfeito()
    
    
    def processar_reproducao(self, animal, vizinhos):
        return None
    
    def processar_movimento(self, animal):
           movimentos = [(0,1) , (0,-1)  , (1,0)  , (-1,0)]
           dx , dy = random.choice(movimentos)
           return Posicao(animal.posicao.x + dx, animal.posicao.y + dy)
       
    def gastar_energia(self, animal):
            return super().gastar_energia(animal)
       
       
class Descansando(EstadoAnimal):
    def processar_fome(self, animal, vizinhos):
        if animal.energia < (animal.ENERGIA_INICIAL * const.ENTRAR_ESTADO_SATISFEITO):
            animal.estado = Satisfeito()
    
    def processar_reproducao(self, animal, vizinhos):
        filhote = animal.executar_reproducao(vizinhos)
        return filhote
    
    def processar_movimento(self, animal):
        
        return Posicao(animal.posicao.x , animal.posicao.y)
    
    def gastar_energia(self, animal):
        
        animal.energia -= (animal.consumo_energia * const.REDUCAO_ENERGIA_ESTADO_DESCANSO)
        if animal.energia <= 0:
            animal.morrer()
            