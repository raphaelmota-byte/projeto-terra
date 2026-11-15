import { useState } from 'react';

export function LogMundo({ logs }) {
  // Controla se a caixa de histórico está visível ou recolhida
  const [aberto, setAberto] = useState(false);

  // Define a cor do texto conforme o tipo de acontecimento
  const obterCorEvento = (texto) => {
    if (texto.includes('tentou mas não predou')) return 'text-warning-emphasis';
    if (texto.includes('predou')) return 'text-danger fw-semibold';
    if (texto.includes('nasceu')) return 'text-success fw-semibold';
    if (texto.includes('comeu') || texto.includes('devorou')) return 'text-primary';
    return 'text-dark';
  };

  return (
    <div className="d-flex flex-column align-items-center my-3 w-100">
      {/* Botão que alterna entre abrir e fechar a caixa */}
      <button
        className="btn btn-outline-dark fw-bold d-flex align-items-center gap-2 shadow-sm"
        onClick={() => setAberto(!aberto)}
      >
        <span>📜 {aberto ? 'Ocultar Log do Mundo' : 'Ver Log do Mundo'}</span>
        <span className="badge bg-secondary rounded-pill">{logs.length}</span>
      </button>

      {/* Caixa retrátil renderizada apenas quando 'aberto' for true */}
      {aberto && (
        <div
          className="card shadow-sm mt-2 border-secondary"
          style={{ width: '100%', maxWidth: '600px' }}
        >
          <div className="card-header bg-dark text-white d-flex justify-content-between align-items-center py-2">
            <span className="fw-bold small">Eventos Recentes (Últimos 50)</span>
            <span className="badge bg-light text-dark">Mais recente no topo</span>
          </div>

          <div
            className="card-body p-2 text-start bg-light"
            style={{ maxHeight: '240px', overflowY: 'auto' }}
          >
            {logs.length === 0 ? (
              <p className="text-muted text-center my-3 small">
                Nenhuma interação registrada ainda. Avance alguns turnos!
              </p>
            ) : (
              <ul className="list-group list-group-flush">
                {logs.map((evento, index) => (
                  <li
                    key={index}
                    className={`list-group-item bg-transparent py-1 px-2 small font-monospace ${obterCorEvento(evento)}`}
                  >
                    {evento}
                  </li>
                ))}
              </ul>
            )}
          </div>
        </div>
      )}
    </div>
  );
}