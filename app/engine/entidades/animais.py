from .entidades import SerVivo
from .estados import Satisfeito
from ..mundo.posicao import Posicao
from ..config import constantes as const
import random
 
class Animal(SerVivo):
    PERCEPCAO = 0
    
    def __init__(self, posicao_obj:Posicao , energia_inicial , consumo_energia , consumo_reproducao, genero=None ):
        super().__init__(posicao_obj)
        self.energia = energia_inicial
        self.consumo_energia = consumo_energia
        self.consumo_reproducao = consumo_reproducao
        self.genero = genero if genero else random.choice(["M" , "F"])
        self.estado = Satisfeito()
        
    def escolher_proximo_passo(self):
        movimentos = [(0,1) , (0,-1)  , (1,0)  , (-1,0)]
        dx , dy = random.choice(movimentos)
        return Posicao(self.posicao.x + dx, self.posicao.y + dy)
        

    def gastar_energia(self):
        self.energia -= self.consumo_energia
        if self.energia <= 0:
            self.morrer()
    
    def alimentar(self , vizinhos):
        self.estado.processar_fome(self, vizinhos)
        
    def executar_alimentacao(self , vizinhos):
        for vizinho in vizinhos:
          if vizinho.__class__.__name__ == self.alvo_presa: #type:ignore
            dado = random.randint(1, 100)
            # print(f" -> Dado rolou {dado} (precisava de <= {self.chance_predacao})")
            if dado <= self.chance_predacao: #type:ignore
                vizinho.morrer()  # A presa tem o status vivo=False e será limpa pelo motor
                
                valor_base = vizinho.ENERGIA_INICIAL 
                bonus_gordura = vizinho.energia * const.BONUS_GORDURA 
                total_refeicao = valor_base + bonus_gordura
                
                self.energia = min(self.energia + total_refeicao , self.ENERGIA_INICIAL) #type:ignore
                
            break
        
    def reproduzir(self, vizinhos):
        return self.estado.processar_reproducao(self , vizinhos)
        
    def executar_reproducao(self , vizinhos):
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
    CHANCE_PREDACAO = const.CHANCE_PREDACAO_COELHO_ARVORE
    
    def __init__(self , posicao_obj , genero=None):
        super().__init__(posicao_obj , genero=genero , energia_inicial=self.ENERGIA_INICIAL , consumo_energia=self.CONSUMO_ENERGIA , consumo_reproducao = self.CONSUMO_REPRODUCAO)
        self.icone = "🐇" if self.genero == "M" else "🐰"
        self.alvo_presa = "Planta"
        self.chance_predacao = self.CHANCE_PREDACAO
        
    def executar_alimentacao(self, vizinhos):
        for vizinho in vizinhos:
            # 1. Filtro da Dieta (Garante que só come Planta)
            if vizinho.__class__.__name__ == self.alvo_presa:
                
                # LOG: Mostra o coelho achando a planta
                # print(f"[Coelho ({self.energia} energia)] começou a comer uma Planta (Tamanho atual: {vizinho.tamanho:.1f})!")
                
                # 2. O Consumo (Sem probabilidade de erro)
                # O coelho tira uma "mordida" fixa do tamanho da planta
                mordida = const.MORDIDA_COELHO 
                vizinho.tamanho -= mordida
                
                # 3. Verificação de Morte da Planta
                if vizinho.tamanho <= 0:
                    vizinho.morrer() # A planta foi totalmente devorada e sairá do mapa
                    # print(" -> A planta foi totalmente consumida e morreu!")
                
                # A Digestão
                ganho_por_mordida = const.GANHO_ENERGIA_MORDIDA 
                self.energia = min(self.energia + ganho_por_mordida, self.ENERGIA_INICIAL)
                
                # print(f" -> REFEIÇÃO SUCESSO! Nova energia do coelho: {self.energia}")
                
               
                break
        
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
    CHANCE_PREDACAO = const.CHANCE_PREDACAO_COBRA_COELHO
    
    def __init__(self , posicao_obj , genero=None):
        super().__init__(posicao_obj , genero=genero , energia_inicial=self.ENERGIA_INICIAL , consumo_energia=self.CONSUMO_ENERGIA , consumo_reproducao = self.CONSUMO_REPRODUCAO)
        self.icone = "🐍" if self.genero == "M" else "🐉"
        self.alvo_presa = "Coelho"
        self.chance_predacao = self.CHANCE_PREDACAO
    
    
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
    CHANCE_PREDACAO = const.CHANCE_PREDACAO_GAVIAO_COBRA
    
    def __init__(self , posicao_obj , genero=None):
        super().__init__(posicao_obj , genero=genero , energia_inicial=self.ENERGIA_INICIAL , consumo_energia=self.CONSUMO_ENERGIA , consumo_reproducao = self.CONSUMO_REPRODUCAO)
        self.icone = "🦅" if self.genero == "M" else "🐦"
        self.alvo_presa = "Cobra"
        self.chance_predacao = self.CHANCE_PREDACAO
    
    def __str__(self) -> str:
        return super().__str__()
    
    def to_dict(self):
        dados = super().to_dict()
        dados.update({"icone" : self.icone})
        return dados