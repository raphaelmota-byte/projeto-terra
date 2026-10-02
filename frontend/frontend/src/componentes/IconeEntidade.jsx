
import './style/IconeEntidade.css'
import coelho_icone from '../assets/coelho_icone.svg'
import cobra_icone from '../assets/cobra_icone.svg'
import gaviao_icone from '../assets/gaviao_icone.svg'
import arvore_icone from '../assets/arvore_icone.svg'

// 2. Dicionário de caminhos de imagens
const mapaDeIcones = {
  coelho: coelho_icone,
  cobra: cobra_icone,
  gaviao: gaviao_icone ,
  planta: arvore_icone ,
};

export const IconeEntidade = ({ entidades }) => {
  if (!entidades || entidades.length === 0) return null;

  try {
    const ultimaEntidade = entidades[entidades.length - 1];
    const nomeAnimal = ultimaEntidade?.nome_entidade?.[0]?.toLowerCase();
    const genero = ultimaEntidade?.genero;

    if (!nomeAnimal) return null;

    const srcDaImagem = mapaDeIcones[nomeAnimal];

    if (!srcDaImagem) {
      return (
        <div className="fw-bold text-dark" title={`Gênero: ${genero}`}>
          {nomeAnimal.charAt(0).toUpperCase()} 
        </div>
      );
    }

    // Se for fêmea, aplica a classe especial
    const ehFemea = genero === 'F';
    const classeFemea = ehFemea ? 'estilo-femea' : '';

    let textoTooltip = `Espécie: ${nomeAnimal}`;
    
    if (genero) {
        textoTooltip += ` | Sexo: ${ehFemea ? 'Fêmea' : 'Macho'}`;
    }
    if (ultimaEntidade?.energia !== undefined) {
        textoTooltip += ` | Energia: ${ultimaEntidade.energia}`;
    }
    if (ultimaEntidade?.tamanho !== undefined) {
        textoTooltip += ` | Tamanho: ${ultimaEntidade.tamanho}`; // Exibe o tamanho da planta!
    }

    return (
      <img 
        src={srcDaImagem} 
        alt={nomeAnimal} 
        title={textoTooltip} 
        className={`icon-entidade ${classeFemea}`} 
      />
    );

  } catch (erro) {
    console.error("Erro ao desenhar entidade:", erro);
    return null;
  }
};