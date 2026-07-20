from entidades.planta import Planta
from entidades.animais import Coelho , Cobra , Gaviao
from mundo.posicao import Posicao
from mundo.mapa import Mapa
from entidades.entidades import SerVivo
from mundo.mundo import Mundo




mapa = Mapa(16 , 16 )
mundo = Mundo(mapa)




coelho = Coelho(Posicao(1,1))
cobra = Cobra(Posicao(1,1))
gaviao = Gaviao(Posicao(1,1))


mundo.adicionar_entidade(coelho)
mundo.adicionar_entidade(cobra)
mundo.adicionar_entidade(gaviao)


# mundo.remover_entidade(coelho)

celula = mapa.obter_celula(coelho.posicao)

for _ in range(1,7):
    mundo.atualizar()
    
for entidade in celula.entidades:
    print(entidade)
    print(f"energia inicial:{entidade.ENERGIA_INICIAL}")
    print(f"energia atual:{entidade.energia}")
    print(f"percepção:{entidade.PERCEPCAO}")
    print(f"consumo de energia:{entidade.CONSUMO_ENERGIA}")
    print("--"*60)