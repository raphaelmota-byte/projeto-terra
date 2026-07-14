from mundo.mapa import Mapa


mapa = Mapa(16 , 16 )
print(mapa)

for linhas in mapa.celulas:
    print(*linhas)
    
mapa.gerar_agua()

print("--" * 60)

for linhas in mapa.celulas:
    print(*linhas)

from entidades.entidades import Posicao  , Planta

posicao_generica = Posicao(2, 1)

planta = Planta(posicao_generica)
print(planta)

planta.envelhecer()
print(planta)