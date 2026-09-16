from app.engine.entidades.entidades import SerVivo
from app.engine.mundo.posicao import Posicao
import app.engine.config.constantes as const
import random
 
class Animal(SerVivo):
    PERCEPCAO = 0
    
    def __init__(self, posicao_obj:Posicao , energia_inicial , consumo_energia , consumo_reproducao, genero=None ):
        super().__init__(posicao_obj)
        self.energia = energia_inicial
        self.consumo_energia = consumo_energia
        self.consumo_reproducao = consumo_reproducao
        self.genero = genero if genero else random.choice(["M" , "F"])
        
    def escolher_proximo_passo(self):
        movimentos = [(0,1) , (0,-1)  , (1,0)  , (-1,0)]
        dx , dy = random.choice(movimentos)
        return Posicao(self.posicao.x + dx, self.posicao.y + dy)
        

    def gastar_energia(self):
        self.energia -= self.consumo_energia
        if self.energia <= 0:
            self.morrer()
    
    def alimentar(self):
        pass

    def reproduzir(self, vizinhos):
        # 1. Apenas fêmeas dão à luz
        if self.genero != "F":
            return None
            
        # 2. Checa se a fêmea tem energia baseada na sua espécie
        if self.energia >= self.consumo_reproducao:
            
            # 3. Procura um macho da MESMA ESPÉCIE
            tem_macho_perto = False
            for vizinho in vizinhos:
                # type(vizinho) is type(self) garante que Coelho só cruza com Coelho!
                if type(vizinho) is type(self) and vizinho.genero == "M" and vizinho.estar_vivo():
                    tem_macho_perto = True
                    break
            
            if tem_macho_perto:
                # Gasta a energia da mãe
                self.energia -= self.consumo_reproducao / 2
                
                # type(self) vira a classe atual. Se self é Coelho, isso vira Coelho(...)
                filhote = type(self)(Posicao(self.posicao.x, self.posicao.y)) #type:ignore
                
                return filhote
                
        return None
    
    def atualizar(self):
        super().atualizar()
        self.gastar_energia()
        
    def to_dict(self):
        dados = super().to_dict()
        dados.update({
            "energia" : self.energia ,
            "consumo_energia" : self.consumo_energia ,
            "consumo_reproducao" :  self.consumo_reproducao ,
            "genero" : self.genero
        })
        return dados


class Coelho(Animal):
    PERCEPCAO = const.PERCEPCAO_COELHO
    ENERGIA_INICIAL = const.ENERGIA_INICIAL_COELHO
    CONSUMO_ENERGIA = const.CONSUMO_ENERGIA_COELHO
    CONSUMO_REPRODUCAO = const.ENERGIA_REPRODUCAO_COELHO
    
    def __init__(self , posicao_obj , genero=None):
        super().__init__(posicao_obj , genero=genero , energia_inicial=self.ENERGIA_INICIAL , consumo_energia=self.CONSUMO_ENERGIA , consumo_reproducao = self.CONSUMO_REPRODUCAO)
        self.icone = "🐇" if self.genero == "M" else "🐰"
   
    
        
    def __str__(self) -> str:
        return f"{super().__str__()}"
    
    def to_dict(self):
        dados = super().to_dict()
        dados.update({"icone" : self.icone})
        return dados
    
class Cobra(Animal):
    PERCEPCAO = const.PERCEPCAO_COBRA
    ENERGIA_INICIAL = const.ENERGIA_INICIAL_COBRA
    CONSUMO_ENERGIA = const.CONSUMO_ENERGIA_COBRA
    CONSUMO_REPRODUCAO = const.ENERGIA_REPRODUCAO_COBRA
    
    def __init__(self , posicao_obj , genero=None):
        super().__init__(posicao_obj , genero=genero , energia_inicial=self.ENERGIA_INICIAL , consumo_energia=self.CONSUMO_ENERGIA , consumo_reproducao = self.CONSUMO_REPRODUCAO)
        self.icone = "🐍" if self.genero == "M" else "🐉"
        
    def __str__(self) -> str:
        return f"{super().__str__()}"
    
    def to_dict(self):
           dados = super().to_dict()
           dados.update({"icone" : self.icone})
           return dados
        
        
class Gaviao(Animal):
    PERCEPCAO = const.PERCEPCAO_GAVIAO
    ENERGIA_INICIAL = const.ENERGIA_INICIAL_GAVIAO
    CONSUMO_ENERGIA = const.CONSUMO_ENERGIA_GAVIAO
    CONSUMO_REPRODUCAO = const.ENERGIA_REPRODUCAO_GAVIAO
    
    def __init__(self , posicao_obj , genero=None):
        super().__init__(posicao_obj , genero=genero , energia_inicial=self.ENERGIA_INICIAL , consumo_energia=self.CONSUMO_ENERGIA , consumo_reproducao = self.CONSUMO_REPRODUCAO)
        self.icone = "🦅" if self.genero == "M" else "🐦"
    
    def __str__(self) -> str:
        return super().__str__()
    
    def to_dict(self):
        dados = super().to_dict()
        dados.update({"icone" : self.icone})
        return dados