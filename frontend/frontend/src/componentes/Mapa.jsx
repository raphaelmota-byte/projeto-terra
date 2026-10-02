import './style/mapa.css'
import {IconeEntidade} from './IconeEntidade'

export const Mapa = ({mundo}) => {
    if (!mundo || mundo.length === 0) {
        return null; 
    }

    return (
        <div className="mt-4 d-flex flex-column align-items-center">
            <h3 className="mb-3">Mapa do Ecossistema</h3>
            
            <div className="mapa-container">
                <div 
                    className="tabuleiro" 
                    style={{ gridTemplateColumns: `repeat(${mundo[0].length}, 30px)` }} 
                >
                    {mundo.map((linha, indexLinha) => (
                        linha.map((celula, indexColuna) => {
                            return (
                                <div 
                                    key={`${indexLinha}-${indexColuna}`} 
                                    className={`celula terreno-${celula.tipo}`}
                                    title={`Posição: ${celula.posicao.x}x${celula.posicao.y}`}
                                > 
                                    <IconeEntidade entidades={celula.entidades_celula} />
                                </div>  
                            );
                        })
                    ))}
                </div>
            </div>
        </div>
    );
}