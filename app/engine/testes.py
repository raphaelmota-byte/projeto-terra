import time
import os

from entidades.animais import Coelho , Cobra , Gaviao
from entidades.planta import Planta
from mundo.posicao import Posicao
from mundo.mapa import Mapa
from mundo.mundo import Mundo
import random



tamanho_mapa = 10
tamanho_mapa_lim = tamanho_mapa-1

mapa = Mapa(tamanho_mapa , tamanho_mapa )
mundo = Mundo(mapa)
print(mapa)




for i in range(11):
    cord_x = random.randint(0 , tamanho_mapa_lim)
    cord_y = random.randint(0 , tamanho_mapa_lim)
    mundo.adicionar_entidade(Coelho(Posicao(cord_x , cord_y)))

# 2. Criando as Cobras na posição (1, 1) - Casal
for i in range(9):
    cord_x = random.randint(0 , tamanho_mapa_lim)
    cord_y = random.randint(0 , tamanho_mapa_lim)
    mundo.adicionar_entidade(Cobra(Posicao(cord_x , cord_y)))
    

for i in range(5):
    cord_x = random.randint(0 , tamanho_mapa_lim)
    cord_y = random.randint(0 , tamanho_mapa_lim)
    mundo.adicionar_entidade(Gaviao(Posicao(cord_x , cord_y)))


ciclo = 1

while True:
    # 1. Limpa a tela do terminal (cls para Windows, clear para Linux/Mac)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # 2. Imprime o status visual atualizado
    print(f"--- TURNO {ciclo} ---")
    print(f"Animais vivos: {len(mundo.entidades_mundo)}")
    print(mapa)
    
    # for entidade in mundo.entidades_mundo:
    # O print(entidade) roda para todos, pois chama o __str__ que toda classe tem
        # print(entidade)

        # Se a entidade tiver o atributo 'energia', sabemos que é um Animal
        # if hasattr(entidade, "energia"):
        #     print(f"energia inicial: {entidade.ENERGIA_INICIAL}")
        #     print(f"energia atual: {entidade.energia}")
        #     print(f"percepção: {entidade.PERCEPCAO}")
        #     print(f"consumo de energia: {entidade.CONSUMO_ENERGIA}")
        #     print(f"genero do animal: {entidade.genero}")

        # # Se a entidade tiver o atributo 'tamanho', sabemos que é uma Planta
        # elif hasattr(entidade, "tamanho"):
        #     print(f"tamanho atual: {entidade.tamanho}")

        # print("--"*60)
    
    mundo.atualizar()
    
    # 4. Condição de parada de segurança
    if len(mundo.entidades_mundo) == 0 or ciclo >= 10:
        print("\nO ecossistema entrou em colapso. Todos os animais morreram.")
        break
        
    ciclo += 1
    
    time.sleep(3)