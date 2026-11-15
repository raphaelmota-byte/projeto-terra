import './style/IconeEntidade.css'
import coelho_icone from '../assets/coelho_icone.svg'
import cobra_icone from '../assets/cobra_icone.svg'
import gaviao_icone from '../assets/gaviao_icone.svg'
import arvore_icone from '../assets/arvore_icone.svg'

const mapaDeIcones = {
  coelho: coelho_icone,
  cobra: cobra_icone,
  gaviao: gaviao_icone,
  planta: arvore_icone,
};

export const IconeEntidade = ({ entidades }) => {
  if (!Array.isArray(entidades) || entidades.length === 0) return null;

  const ultimaEntidade = entidades[entidades.length - 1];
  const nomeAnimal = typeof ultimaEntidade?.nome_entidade === 'string'
    ? ultimaEntidade.nome_entidade.toLowerCase()
    : null;
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
    textoTooltip += ` | Tamanho: ${ultimaEntidade.tamanho}`;
  }
  if (ultimaEntidade?.estado !== undefined){
    textoTooltip += ` | Estado: ${ultimaEntidade.estado}`;
  }

  return (
    <img
      src={srcDaImagem}
      alt={nomeAnimal}
      title={textoTooltip}
      className={`icon-entidade ${classeFemea}`}
    />
  );
};