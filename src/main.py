import time
import os

from entidades.animais import Coelho , Cobra , Gaviao
from mundo.posicao import Posicao
from mundo.mapa import Mapa
from mundo.mundo import Mundo




mapa = Mapa(16 , 16 )
mundo = Mundo(mapa)
print(mapa)



coelho = Coelho(Posicao(1,2))
cobra = Cobra(Posicao(1,1))
gaviao = Gaviao(Posicao(1,3))


mundo.adicionar_entidade(coelho)
mundo.adicionar_entidade(cobra)
mundo.adicionar_entidade(gaviao)


# mundo.remover_entidade(coelho)

celula = mapa.obter_celula(coelho.posicao)


    
    
for entidade in celula.entidades:
    print(entidade)
    print(f"energia inicial:{entidade.ENERGIA_INICIAL}")
    print(f"energia atual:{entidade.energia}")
    print(f"percepção:{entidade.PERCEPCAO}")
    print(f"consumo de energia:{entidade.CONSUMO_ENERGIA}")
    print("--"*60)
    
ciclo = 1

# Loop infinito até que uma condição de parada aconteça
while True:
    # 1. Limpa a tela do terminal (cls para Windows, clear para Linux/Mac)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # 2. Imprime o status visual atualizado
    print(f"--- TURNO {ciclo} ---")
    print(f"Animais vivos: {len(mundo.entidades_mundo)}")
    print(mapa)
    
    # 3. Atualiza a lógica do ecossistema (envelhece, gasta energia, mata quem zerou)
    mundo.atualizar()
    
    # 4. Condição de parada de segurança
    if len(mundo.entidades_mundo) == 0:
        print("\nO ecossistema entrou em colapso. Todos os animais morreram.")
        break
        
    ciclo += 1
    
    # 5. Pausa por meio segundo antes de ir para o próximo turno
    time.sleep(3)