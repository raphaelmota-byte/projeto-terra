from ..mundo.posicao import Posicao
from ..config import constantes as const
from typing import Any

class Entidade:
    __slots__ = ['posicao' , 'nome']
    
    def __init__(self , posicao_obj:Posicao ):
        self.posicao = posicao_obj
        self.nome = self.__class__.__name__
    
    def to_dict(self):
        return {
            "posicao_entidade" : self.posicao.to_dict() ,
            "nome_entidade" : self.nome
            }
    
    def __repr__(self):
        return f"{self.nome}(posicao=({self.posicao.x},{self.posicao.y})"
       
        

class SerVivo(Entidade):
    __slots__ = ['horas' , 'vivo']
    def __init__(self , posicao_obj:Posicao):
        super().__init__(posicao_obj)
        self.horas:int = 0
        self.vivo:bool = True
        
    def mostrar_idade(self):
        dias =  (self.horas//24)
        meses = (dias//30)
        anos =  (meses//12)
        
        return f"{self.horas % 24} horas | {dias % 30} dias | { meses % 12} meses| {anos} anos"
        
    def envelhecer(self) -> None:
        self.horas += 3
       
    
    def morrer(self):
        self.vivo = False
    
    def estar_vivo(self):
        return self.vivo
    
    def reproduzir(self , vizinhos):
            #vazio para ser rescrita pelos filhos
        return None
        
    def atualizar(self ):
        self.envelhecer()
        
    def __str__(self) -> str:
        return ( 
            f"Espécie:{self.__class__.__name__} | "
            f"Tempo de vida: {self.mostrar_idade()} | "
            f"Vivo:{self.vivo} | "
            f"Posição:{self.posicao}" 
            )
    
    def __repr__(self) -> str:
        return super().__repr__()
    
    def to_dict(self):
        dados: dict[str , Any] = super().to_dict()
        
        dados.update({
            "vivo" : self.vivo ,
            "horas_vida" : self.horas ,
            "idade_formatada" : self.mostrar_idade()
        })
        
        return dados

# Arquitetura do Projeto Terra

## 1. Visão geral e camadas

O projeto está organizado em três áreas:

- **Core Engine (`app/engine`)**: implementa o domínio da simulação — entidades, estados, mapa, posições e avanço do mundo.
- **API (`app/main.py`)**: expõe operações HTTP com FastAPI, cria e mantém a simulação ativa e delega sua evolução ao engine. Os modelos de entrada estão em `app/schemas.py`.
- **Frontend (`frontend`)**: aplicação React configurada com Vite. A estrutura inclui `App.jsx` e componentes para controle, mapa e representação visual de entidades. Como o conteúdo desses arquivos não foi fornecido, o comportamento detalhado da interface e suas chamadas à API não pode ser confirmado aqui.

O fluxo arquitetural esperado é: o frontend envia comandos à API; a API chama o engine; e o estado resultante é serializado para ser retornado ao frontend.

## 2. Core Engine: entidades e otimização de memória

### 2.1 Hierarquia de classes

```text
Entidade
└── SerVivo
    ├── Animal
    │   ├── Coelho
    │   ├── Cobra
    │   └── Gaviao
    └── Planta
```

- **`Entidade`** define posição e nome.
- **`SerVivo`** acrescenta idade em horas, condição de vida, envelhecimento e operações comuns aos seres vivos.
- **`Animal`** adiciona energia, consumo, gênero e estado comportamental. Coelho, Cobra e Gaviao especializam parâmetros, presa, percepção e ícone.
- **`Planta`** acrescenta tamanho e crescimento.

### 2.2 `__slots__`

As classes da hierarquia declaram `__slots__` para enumerar seus atributos de instância. Como as subclasses também declaram seus próprios slots, essa hierarquia evita, em geral, a criação de um `__dict__` para cada instância e pode reduzir o consumo de memória quando há muitas entidades.

O benefício se aplica à hierarquia de entidades mostrada; outras classes, como `Posicao` e `Celula`, não declaram `__slots__`.

### 2.3 Serialização em cascata

Os métodos `to_dict()` compõem os dados de cada classe por herança:

1. `Entidade.to_dict()` serializa posição e nome.
2. `SerVivo.to_dict()` acrescenta condição de vida e idade.
3. `Animal.to_dict()` acrescenta energia, consumos, gênero e percepção.
4. As classes concretas de animais acrescentam o ícone.
5. `Planta.to_dict()` acrescenta o tamanho.
6. `Celula.to_dict()` serializa suas entidades; `Mapa.to_dict()` serializa as células; `Mundo.to_dict()` inclui o mapa, o total de entidades e as horas passadas.

A posição possui seu próprio `to_dict()`, que retorna as coordenadas `x` e `y`. A planta define um ícone, mas seu `to_dict()` atual não o inclui.

## 3. Padrão State: estados dos animais

`EstadoAnimal` é uma classe abstrata que define o contrato comportamental:

- `processar_fome(animal, vizinhos)`
- `processar_reproducao(animal, vizinhos)`
- `processar_movimento(animal, radar)`
- `gastar_energia(animal)`

Os estados concretos são `Satisfeito`, `Cacando` e `Descansando`. `Cacando` é o nome usado atualmente no código, no lugar de `Faminto`.

| Estado | Fome/alimentação | Reprodução | Movimento | Energia |
|---|---|---|---|---|
| `Satisfeito` | Muda para `Cacando` quando a energia fica abaixo ou igual ao limiar `ENTRAR_ESTADO_CACANDO`; muda para `Descansando` quando fica acima ou igual a `ENTRAR_ESTADO_DESCANSO`. | Delega a `Animal.executar_reproducao()`. | Usa a implementação-base, que escolhe um movimento cardinal aleatório. | Consumo normal. |
| `Cacando` | Executa a alimentação e muda para `Satisfeito` ao atingir o limiar `ENTRAR_ESTADO_SATISFEITO`. | Não reproduz. | Usa a implementação-base. | Consumo normal. |
| `Descansando` | Muda para `Satisfeito` quando a energia fica abaixo do limiar `ENTRAR_ESTADO_SATISFEITO`. | Delega a `Animal.executar_reproducao()`. | Permanece na posição atual. | Consumo reduzido por `REDUCAO_ENERGIA_ESTADO_DESCANSO`. |

Os limiares são definidos em `app/engine/config/constantes.py`; seus valores não estão incluídos neste material. A classe `Animal` delega ao estado atual as operações de fome/alimentação, reprodução, movimento e gasto de energia.

## 4. Motor espacial e percepção

O mapa é uma matriz de células: `y` seleciona a linha e `x` a coluna. Cada célula contém terreno e lista de entidades.

`Mundo.calcular_radar()` usa o atributo `percepcao` da entidade como raio. Calcula os limites de cada eixo e os restringe às dimensões do mapa:

```text
inicio_x = max(0, x - raio)
fim_x    = min(largura, x + raio + 1)

inicio_y = max(0, y - raio)
fim_y    = min(comprimento, y + raio + 1)
```

Os intervalos são percorridos com `range`, cujo limite final não é incluído; por isso, o `+ 1` contempla a coordenada extrema do raio. As travas `max` e `min` mantêm a consulta dentro da matriz e evitam índices fora dos limites, que causariam `IndexError`.

O radar percorre uma área quadrada em torno da entidade e agrega as outras entidades encontradas nas células. Entidades sem `percepcao` recebem uma lista vazia. Embora o radar seja passado ao método de movimento, a implementação-base atual escolhe uma direção cardinal aleatória e não consulta o conteúdo do radar.

## 5. Ciclo de atualização do mundo

Um tick equivale a **3 horas simuladas**. `Mundo.atualizar()` executa as seguintes etapas:

1. Avança `horas_passadas` em 3.
2. Cria uma cópia do conjunto de entidades para iterar enquanto o mundo pode mudar.
3. Ignora entidades já mortas.
4. Executa a predação/alimentação na célula atual.
5. Atualiza a entidade: seres vivos envelhecem 3 horas; animais também gastam energia, e plantas crescem.
6. Se a entidade continua viva, tenta reproduzi-la. O filhote, quando produzido, é adicionado ao mundo.
7. Se a entidade oferece `escolher_proximo_passo`, calcula o radar, escolhe uma posição e tenta movê-la. A movimentação rejeita posições fora do mapa e células de água.
8. Remove do mundo e do mapa as entidades mortas.

A ordem de iteração é a do conjunto `entidades_mundo`, não uma sequência explicitamente ordenada. Isso é relevante para interações entre entidades no mesmo tick.

### Determinismo

O ciclo é discreto, mas **não é totalmente determinístico na implementação atual**. Há fontes de aleatoriedade, incluindo geração de água, posições iniciais, gênero, movimento e probabilidade de predação. Além disso, a iteração sobre um conjunto não define uma ordem de atualização estável. O código da geração de água também contém um comentário indicando a ausência de uma seed fixa.

Para tornar execuções reproduzíveis, seria necessário controlar a aleatoriedade com uma seed e definir uma ordem explícita para processar as entidades.

## 6. API FastAPI

`app/main.py` disponibiliza três rotas:

- **`POST /iniciar`**: cria um mapa quadrado, instancia um novo `Mundo` e distribui coelhos, cobras, gaviões e árvores em posições de terra aleatórias. Os valores padrão do modelo `IniciarMundo` são mapa 16×16, 11 coelhos, 9 cobras, 5 gaviões e 10 árvores.
- **`POST /tick`**: recebe a quantidade de ticks e chama `Mundo.atualizar()` essa quantidade de vezes. Retorna mensagem e tempo de processamento em milissegundos. Se o mundo não foi iniciado, retorna HTTP 404.
- **`GET /estado`**: retorna a serialização do mundo atual. Se não há simulação ativa, retorna HTTP 404.

A instância da simulação é mantida na variável global `simulacao_atual`. Portanto, o estado é compartilhado no processo do servidor, e iniciar outro mundo substitui a simulação anterior. Os schemas de entrada são definidos em `app/schemas.py`: `IniciarMundo` e `AvancaTick`.

A API configura CORS para aceitar qualquer origem, método e cabeçalho; essa configuração deve ser revista antes de um uso exposto em produção.

## 7. Frontend React

A estrutura fornecida indica uma aplicação React com Vite:

- `src/App.jsx`: componente principal da aplicação.
- `src/componentes/Controle.jsx`: componente de controle, conforme sua organização e nome.
- `src/componentes/Mapa.jsx`: componente de apresentação do mapa.
- `src/componentes/IconeEntidade.jsx`: componente associado à representação de entidades.
- `src/index.css` e `src/componentes/style/`: estilos globais e estilos dos componentes.

Sem o conteúdo dos arquivos do frontend, não é possível documentar com segurança os detalhes do estado React, das requisições HTTP, do formato efetivamente consumido ou das interações da interface.



