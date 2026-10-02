import './style/mapa.css'
import {IconeEntidade} from './IconeEntidade'

export  const  Mapa = ({mundo}) => {
    if (!mundo || mundo.length === 0) {
    return null; 
  }
    return(
        <div className="mt-4 d-flex flex-column align-items-center">
            <h3 className="mb-3">Mapa do Ecossistema</h3>
      
            <div className="tabuleiro">
                {mundo.map((linha, indexLinha) => 
                (
                    linha.map((celula, indexColuna) => 
                    {
            
                    // Aqui entra a sua lógica de cores baseada na célula
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
    );
}