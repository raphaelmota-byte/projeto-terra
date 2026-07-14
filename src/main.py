from entidades.entidades import Posicao  , Planta , Coelho



from mundo.mapa import Mapa

mapa = Mapa(16 , 16 )

print("--" * 60)

planta = Planta(Posicao(1,1))
# print(planta)

mapa.adicionar_entidade(planta)


coelho = Coelho(Posicao(1,1))
coelho_2 = Coelho(Posicao(1,1))
coelho_3 = Coelho(Posicao(1,1))

mapa.adicionar_entidade(coelho)
mapa.adicionar_entidade(coelho_2)
mapa.adicionar_entidade(coelho_3)

celula = mapa.obter_celula(coelho.posicao)
celula = mapa.obter_celula(coelho_2.posicao)
celula = mapa.obter_celula(coelho_3.posicao)

for entidade in celula.entidades:
    print(entidade)
    pass