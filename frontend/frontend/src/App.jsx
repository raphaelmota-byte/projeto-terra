import { useState , useEffect} from 'react'
import axios from 'axios';
import {Controle } from './componentes/Controle'
import {Mapa} from './componentes/Mapa'
import { LogMundo } from './componentes/logMundo';

function App() {
  const [mundo , setMundo] = useState([]);
  const [totalEntidades , setTotalEntidades] = useState(0);
  const [alerta , setAlerta] = useState(null);
  const [quantTick, setQuantTick] = useState(1);
  const [horasMundo , setHorasMundo] = useState(0);
  
  // tamanho mapa padrao
  const [tamMapa , setTamMapa] = useState(16);

  // quantidade de animais padrao
  const [qtdCoelhos, setQtdCoelhos] = useState(11);
  const [qtdCobras, setQtdCobras] = useState(9);
  const[qtdGavioes , setQtdGavioes] = useState(5);
  const[qtdArvores , setQtdArvores] = useState(9);

  const[logs , setLogs] = useState([]);

  const carregarEstado = async () => {
    try{
      const resposta = await axios.get("http://127.0.0.1:8000/estado")
      setMundo(resposta.data.mapa);
      setTotalEntidades(resposta.data.total_entidades);
      setHorasMundo(resposta.data.horas_passadas) ;
      setLogs(resposta.data.logs || []) ;
      setAlerta(null)
    }
    catch(erro){
      console.error("Falha ao carregar estado:", erro);
      setAlerta("O mundo ainda não foi carregador, por favor confira sua conexão ou clique em iniciar.");
    }
  };

  const iniciarSimulacao = async () => {
    try{
      await axios.post("http://127.0.0.1:8000/iniciar", { 
        tamanho_mapa: tamMapa ,
        qtd_coelhos: qtdCoelhos,
        qtd_cobras: qtdCobras ,
        qtd_gavioes : qtdGavioes ,
        qtd_arvores : qtdArvores 
      });
      carregarEstado(); 

    }catch(error){
      console.error("Falha ao carregar estado:", error);
      setAlerta("Erro ao iniciar simulação, por favor confira sua conexão.");
    }
  };

  const avancarTurno = async () => {
    try{
      await axios.post("http://127.0.0.1:8000/tick", { tick: quantTick });
      // Busca o estado atualizado e salva no useState, forçando a tela a refletir a nova realidade
      carregarEstado();

    }catch{
    console.log("Erro ao avançar o turno");
     setAlerta("O mundo ainda não foi iniciado. Clique em 'Iniciar Novo Mundo'.");

    }
  };

  const voltarSetup = () => {
    setMundo([]); // Isso faz a flag mundoAtivo virar false na mesma hora!
    setTotalEntidades(0);
    setHorasMundo(0);
    setLogs([]) ;
  };


  // roda toda vez que a pagina recarregar
  useEffect(() => {
    const carregarEstadoInicial = async () => {
      try {
        const resposta = await axios.get("http://127.0.0.1:8000/estado");
        setMundo(resposta.data.mapa);
        setTotalEntidades(resposta.data.total_entidades);
        setHorasMundo(resposta.data.horas_passadas);
        setLogs(resposta.data.logs || []);
        setAlerta(null);
      } catch (erro) {
        console.error("Falha ao carregar estado inicial:", erro);
        setAlerta("O mundo ainda não foi carregado, por favor confira sua conexão ou clique em iniciar.");
        setLogs([]);
      }
    };

    carregarEstadoInicial();
  }, []);

  const dias = Math.floor(horasMundo / 24);
  const horas = horasMundo % 24;

  return (
    <>
      <div className='container-fluid'>

        <h1 className='display-3'>Projeto Terra</h1>
        
        <div className="lead mt-2 mb-3 d-flex justify-content-center gap-4">
          <span>Total de entidades vivas: <strong>{totalEntidades}</strong></span>
          <span className="border-start border-2 ps-4"> Idade do Mundo: <strong>{dias} dias e {horas} horas</strong> </span>

        </div>


        <Mapa mundo={mundo}/>

        <Controle 
          iniciarSimu={iniciarSimulacao} 
          avancarTurno={avancarTurno} 
          voltarSetup={voltarSetup}
          quantTick={quantTick} 
          setQuantTick={setQuantTick} 
          tamMapa={tamMapa}
          setTamMapa={setTamMapa}

          qtdCoelhos={qtdCoelhos}
          setQtdCoelhos={setQtdCoelhos}

          qtdCobras={qtdCobras}
          setQtdCobras={setQtdCobras}

          qtdGavioes={qtdGavioes}
          setQtdGavioes={setQtdGavioes}

          qtdArvores={qtdArvores}
          setQtdArvores={setQtdArvores}

          mundoAtivo={mundo.length > 0}
        />

        {mundo.length > 0 && <LogMundo logs={logs} />}

        {alerta && (
          <div className="mt-3 alert alert-warning text-center fw-bold">{alerta}</div> //
        )}

      </div>
    </>
    )};

export default App