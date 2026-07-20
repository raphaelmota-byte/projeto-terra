from entidades.planta import Planta
from entidades.animais import Coelho , Cobra , Gaviao
from mundo.posicao import Posicao
from mundo.mapa import Mapa
from entidades.entidades import SerVivo




mapa = Mapa(16 , 16 )

# print(mapa)






coelho = Coelho(Posicao(1,1))
cobra = Cobra(Posicao(1,1))
gaviao = Gaviao(Posicao(1,1))

mapa.adicionar_entidade(coelho)
mapa.adicionar_entidade(cobra)
mapa.adicionar_entidade(gaviao)

celula = mapa.obter_celula(coelho.posicao)

for _ in range(1,100_000):
    coelho.envelhecer()
    
for entidade in celula.entidades:
    print(entidade)
    print(f"energia inicial:{entidade.ENERGIA_INICIAL}")
    print(f"energia atual:{entidade.energia}")
    print(f"percepção:{entidade.PERCEPCAO}")
    print(f"consumo de energia:{entidade.CONSUMO_ENERGIA}")
    print("--"*60)