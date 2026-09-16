from mundo.mapa import Mapa
from entidades.entidades import Entidade
from mundo.posicao import Posicao

class Mundo:
    def __init__(self , mapa_obj:Mapa) -> None:
        self.mapa = mapa_obj # o mundo contem o mapa
        self.entidades_mundo = [] #lista com todas as entidades do mundo
        
    def adicionar_entidade(self , entidade:Entidade): # TODO:adicionar verificações de sucesso entre as funções.Serve para atualizar tanto a lista tanto o mapa
        self.entidades_mundo.append(entidade)
        self.mapa.adicionar_entidade(entidade) 
        
    def remover_entidade(self , entidade:Entidade): # TODO:adicionar verificações de sucesso entre as funções.
        if entidade in self.entidades_mundo:
            self.entidades_mundo.remove(entidade) 
            self.mapa.remover_entidade(entidade) #roda a função da class mapa 
    
    def remover_mortos(self):
        # Copio a lista porque remover_entidade() altera self.entidades_mundo
        # durante o loop — iterar direto pularia elementos.
        
        entidades = self.entidades_mundo.copy()
        for entidade in entidades:
            if not entidade.estar_vivo():
                self.remover_entidade(entidade)
                
    def mover_entidade_fisicamente(self , entidade:Entidade , nova_pos:Posicao):
        #uso o try porque o metodo validar_posicao sobe um error quando falso
        try:
            self.mapa.validar_posicao(nova_pos)
            
            self.mapa.remover_entidade(entidade)
            
            entidade.posicao = nova_pos
    
            self.mapa.adicionar_entidade(entidade)
            
        except IndexError:
            pass
        
    def reproduzir_entidade(self , entidade:Entidade):
        
        celula = self.mapa.obter_celula(entidade.posicao)
        vizinhos = celula.entidades
        
        filho = entidade.reproduzir(vizinhos)#type:ignore
        if filho is not None:
            self.adicionar_entidade(filho)
                    
        
    def atualizar(self):
        entidades = self.entidades_mundo.copy()
        
        for entidade in entidades:
           # 1. Blindagem Zumbi: Se o bicho morreu neste mesmo turno 
            # (ex: foi comido por alguém que agiu antes), ignoramos ele.
            if not entidade.estar_vivo():
                continue
            
            # 2. Atualiza o status básico (gasta energia por existir, envelhece, etc)
            entidade.atualizar()
            
            # 3. Verifica novamente se ele não morreu de velhice/fome no atualizar()
            if entidade.estar_vivo():
                
                # 4. Tenta reproduzir
                self.reproduzir_entidade(entidade)
            
            if hasattr(entidade , "escolher_proximo_passo"): 
                nova_pos = entidade.escolher_proximo_passo()
                self.mover_entidade_fisicamente(entidade , nova_pos)
                
        self.remover_mortos()
        
    def __str__(self):
        return f"o mundo possui {len(self.entidades_mundo)} entidades"