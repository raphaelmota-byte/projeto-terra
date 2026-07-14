from mundo.mapa import Mapa

mapa = Mapa(16 , 16 )
print(mapa)

for linhas in mapa.celulas:
    print(*linhas)
    
mapa.gerar_agua()

print("--" * 60)

for linhas in mapa.celulas:
    print(*linhas)



from entidades.entidades import Posicao  , Planta , Coelho


planta = Planta(Posicao(2,1))
print(planta)

planta.envelhecer()
print(planta)

coelho = Coelho(Posicao(1,1))
print(coelho.posicao)