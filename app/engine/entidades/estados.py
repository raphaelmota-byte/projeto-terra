from abc import ABC , abstractmethod
import random
from ..mundo.posicao import Posicao
from ..config import constantes as const
from .entidades import SerVivo

#a classe abstrata é o molde e reclama de error se as filhas não rescreverem seus métodos
class EstadoAnimal(ABC):
    
    @abstractmethod
    def processar_fome(self , animal , vizinhos) -> str|None: 
        pass
    
    @abstractmethod
    def processar_reproducao(self, animal, vizinhos):
        pass
    
    @abstractmethod
    def processar_movimento(self , animal , radar):
        movimentos = [(0,1) , (0,-1)  , (1,0)  , (-1,0)]
        dx , dy = random.choice(movimentos)
        return Posicao(animal.posicao.x + dx, animal.posicao.y + dy)
    
    @abstractmethod
    def gastar_energia(self , animal):
        animal.energia -= animal.consumo_energia
        if animal.energia <= 0:
            animal.morrer()

class Satisfeito(EstadoAnimal):
    def processar_fome(self , animal ,  vizinhos) -> None:
        
        if animal.energia <= (animal.ENERGIA_INICIAL * const.ENTRAR_ESTADO_CACANDO):
            animal.estado = Cacando()
        elif animal.energia >= (animal.ENERGIA_INICIAL * const.ENTRAR_ESTADO_DESCANSO):
            animal.estado = Descansando()
        return None
    
    def processar_reproducao(self, animal, vizinhos):
        filhote = animal.executar_reproducao(vizinhos)
        return filhote
    
    def processar_movimento(self, animal , radar):
        return super().processar_movimento(animal , radar)
    
    def gastar_energia(self, animal):
        return super().gastar_energia(animal)
    
class Cacando(EstadoAnimal):
    def processar_fome(self, animal, vizinhos) -> str:
        evento = animal.executar_alimentacao(vizinhos)
        
        if animal.energia >= (animal.ENERGIA_INICIAL * const.ENTRAR_ESTADO_SATISFEITO):
            animal.estado = Satisfeito()
        return evento
    
    def processar_reproducao(self, animal, vizinhos):
        return None
    
    def processar_movimento(self, animal , radar:list[SerVivo]):
        presas = [
            vizinho for vizinho in radar 
            if vizinho.__class__.__name__ == animal.alvo_presa and vizinho.estar_vivo()
        ]

        if not presas:
            return super().processar_movimento(animal , radar)
    
        presa_alvo = min(
            presas , 
            key=lambda p: abs(p.posicao.x - animal.posicao.x) + abs(p.posicao.y - animal.posicao.y)          
            )
               

        dx = 1 if presa_alvo.posicao.x >= animal.posicao.x else -1
        dy = 1 if presa_alvo.posicao.y > animal.posicao.y else -1
        
        distancia_x = abs(presa_alvo.posicao.x - animal.posicao.x)
        distancia_y = abs(presa_alvo.posicao.y - animal.posicao.y)
        
        # 4. Decide o eixo prioritário para o passo
        if distancia_x > distancia_y:
            return Posicao(animal.posicao.x + dx, animal.posicao.y)
        else:
            return Posicao(animal.posicao.x, animal.posicao.y + dy)
    
       
    def gastar_energia(self, animal):
            return super().gastar_energia(animal)
       
       
       
class Descansando(EstadoAnimal):
    def processar_fome(self, animal, vizinhos):
        if animal.energia < (animal.ENERGIA_INICIAL * const.ENTRAR_ESTADO_SATISFEITO):
            animal.estado = Satisfeito()
        return None
    
    def processar_reproducao(self, animal, vizinhos):
        filhote = animal.executar_reproducao(vizinhos)
        return filhote
    
    def processar_movimento(self, animal , radar):
        
        return Posicao(animal.posicao.x , animal.posicao.y)
    
    def gastar_energia(self, animal):
        
        animal.energia -= (animal.consumo_energia * const.REDUCAO_ENERGIA_ESTADO_DESCANSO)
        if animal.energia <= 0:
            animal.morrer()
            