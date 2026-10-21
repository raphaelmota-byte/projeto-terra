import { useEffect } from 'react';

function BlocoControle({ id, label, valor, min, max, onChange, onClick, textoBotao, corBotao }) {
  return (
    <div className="d-flex align-items-center gap-2 bg-white p-2 rounded border shadow-sm">
      <label htmlFor={id} className="text-muted mb-0 fw-bold ms-2">
        {label}:
      </label>

      <input
        id={id}
        type="number"
        className="form-control text-center"
        style={{ width: "80px" }}
        min={min}
        max={max}
        value={valor}
        onChange={(e) => onChange(Number(e.target.value))}
      />
      
      {/* MÁGICA AQUI: O botão só será renderizado se a prop 'textoBotao' for enviada */}
      {textoBotao && (
        <button className={`btn btn-${corBotao} fw-bold px-4`} onClick={onClick}>
          {textoBotao}
        </button>
      )}
    </div>
  );
}

// 2. Componente principal organizado em blocos visuais (Setup vs Tempo)
export function Controle({ 
  iniciarSimu, avancarTurno, 
  quantTick, setQuantTick, 
  tamMapa, setTamMapa,
  qtdCoelhos, setQtdCoelhos,
  qtdCobras, setQtdCobras,
  qtdGavioes, setQtdGavioes,
  qtdArvores, setQtdArvores ,
  mundoAtivo , voltarSetup
}) {

useEffect(() => {
    const lidarComTeclado = (evento) => {
      // Só avança o turno se apertar Enter E se o mundo já estiver ativo
      if (evento.key === 'Enter' && mundoAtivo) {
        avancarTurno();
      }
    };

    window.addEventListener('keydown', lidarComTeclado);
    
    // Limpeza de segurança para evitar que o React dispare a função duas vezes
    return () => {
      window.removeEventListener('keydown', lidarComTeclado);
    };
  }, [avancarTurno, mundoAtivo]);

  return (
    <div className="d-flex flex-column justify-content-center align-items-center gap-4 mb-4 mt-3">
      {!mundoAtivo && (
        <div className="d-flex flex-column align-items-center gap-3 p-4 bg-light border rounded shadow-sm w-100">
          <h5 className="w-100 text-muted fw-bold mb-2 text-center">⚙️ Setup do Ecossistema</h5>

          {/* LINHA 1: 3 itens em cima */}
          <div className="d-flex justify-content-center gap-3 flex-wrap w-100">
            <BlocoControle id="input-tam" label="🗺️ Tamanho" valor={tamMapa} min="2" max="40" onChange={setTamMapa} />
            <BlocoControle id="input-coelhos" label="🐇 Coelhos" valor={qtdCoelhos} min="0" max="100" onChange={setQtdCoelhos} />
            <BlocoControle id="input-cobras" label="🐍 Cobras" valor={qtdCobras} min="0" max="100" onChange={setQtdCobras} />
          </div>

          {/* LINHA 2: 2 itens embaixo */}
          <div className="d-flex justify-content-center gap-3 flex-wrap w-100">
            <BlocoControle id="input-gavioes" label="🦅 Gaviões" valor={qtdGavioes} min="0" max="100" onChange={setQtdGavioes} />
            <BlocoControle id="input-arvores" label="🌳 Árvores" valor={qtdArvores} min="0" max="100" onChange={setQtdArvores} />
          </div>

          {/* Botão principal centralizado abaixo dos inputs */}
          <div className="w-100 d-flex justify-content-center mt-3">
            <button className="btn btn-success btn-lg fw-bold px-5 shadow-sm" onClick={iniciarSimu}>
              🌱 Iniciar Novo Mundo
            </button>
          </div>
        </div>
        )}

      {mundoAtivo && (
          <button 
            className="btn btn-outline-danger fw-bold shadow-sm" 
            onClick={voltarSetup}
            style={{ height: "100%" }} // Para ficar da mesma altura do input
          >
            ⬅️ Voltar ao Setup
          </button>
        )}

      {/* PAINEL 2: Controle do Tempo (Reaproveitando o BlocoControle com botão) */}
      <div className="d-flex flex-wrap justify-content-center">
        <BlocoControle
          id="input-tick"
          label="Avançar no Tempo"
          valor={quantTick}
          min="1"
          max="100"
          onChange={setQuantTick}
          onClick={avancarTurno}
          textoBotao={`⏳ ${quantTick} ${quantTick === 1 ? 'Turno' : 'Turnos'} (${quantTick * 3} horas) -> Enter`}
          corBotao="primary"
        />
      </div>

    </div>
  );
}