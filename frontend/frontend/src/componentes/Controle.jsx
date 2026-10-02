// 1. Criamos o molde reutilizável que serve para qualquer controle numérico
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
      
      <button className={`btn btn-${corBotao} fw-bold px-4`} onClick={onClick}>
        {textoBotao}
      </button>
     
    </div>
  );
}

// 2. O componente principal fica extremamente limpo e fácil de ler
export function Controle({ iniciarSimu, avancarTurno, quantTick, setQuantTick, tamMapa, setTamMapa }) {
  return (
    <div className="d-flex justify-content-center align-items-center gap-4 mb-4 mt-3 flex-wrap">
      
      <BlocoControle
        id="input-tam"
        label="Tamanho"
        valor={tamMapa}
        min="2"
        max="40"
        onChange={setTamMapa}
        onClick={iniciarSimu}
        textoBotao="🌱 Iniciar Novo Mundo"
        corBotao="success"
      />

      <BlocoControle
        id="input-tick"
        label="Avançar"
        valor={quantTick}
        min="1"
        max="100"
        onChange={setQuantTick}
        onClick={avancarTurno}
        textoBotao={`⏳ ${quantTick} ${quantTick === 1 ? 'Turno' : 'Turnos'} (${quantTick * 3} horas)`}
        corBotao="primary"
      />
      

    </div>
  );
}