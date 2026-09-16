import time
import os

from entidades.animais import Coelho , Cobra , Gaviao
from entidades.planta import Planta
from mundo.posicao import Posicao
from mundo.mapa import Mapa
from mundo.mundo import Mundo




mapa = Mapa(16 , 16 )
mundo = Mundo(mapa)
print(mapa)



coelho = Coelho(Posicao(1,2))
cobra = Cobra(Posicao(1,1))
gaviao = Gaviao(Posicao(1,3))
arvore = Planta(Posicao(1,4))


mundo.adicionar_entidade(coelho)
mundo.adicionar_entidade(cobra)
mundo.adicionar_entidade(gaviao)
mundo.adicionar_entidade(arvore)





    
    
    
ciclo = 1

while True:
    # 1. Limpa a tela do terminal (cls para Windows, clear para Linux/Mac)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # 2. Imprime o status visual atualizado
    print(f"--- TURNO {ciclo} ---")
    print(f"Animais vivos: {len(mundo.entidades_mundo)}")
    print(mapa)
    
    for entidade in mundo.entidades_mundo:
    # O print(entidade) roda para todos, pois chama o __str__ que toda classe tem
        print(entidade)

        # Se a entidade tiver o atributo 'energia', sabemos que é um Animal
        if hasattr(entidade, "energia"):
            print(f"energia inicial: {entidade.ENERGIA_INICIAL}")
            print(f"energia atual: {entidade.energia}")
            print(f"percepção: {entidade.PERCEPCAO}")
            print(f"consumo de energia: {entidade.CONSUMO_ENERGIA}")

        # Se a entidade tiver o atributo 'tamanho', sabemos que é uma Planta
        elif hasattr(entidade, "tamanho"):
            print(f"tamanho atual: {entidade.tamanho}")

        print("--"*60)
    
    mundo.atualizar()
    
    # 4. Condição de parada de segurança
    if len(mundo.entidades_mundo) == 0 or ciclo >= 10:
        print("\nO ecossistema entrou em colapso. Todos os animais morreram.")
        break
        
    ciclo += 1
    
    time.sleep(3)