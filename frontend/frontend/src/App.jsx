import { useState , useEffect, useRef} from 'react'
import axios from 'axios';
import {Controle } from './componentes/Controle'
import {Mapa} from './componentes/Mapa'

function App() {
  const [mundo , setMundo] = useState([]);
  const [totalEntidades , setTotalEntidades] = useState(0);
  const [alerta , setAlerta] = useState(null);
  const [quantTick, setQuantTick] = useState(1);
  const [horasMundo , setHorasMundo] = useState(0);
  const [tamMapa , setTamMapa] = useState(16);

  const carregarEstado = async () => {
    try{
      const resposta = await axios.get("http://127.0.0.1:8000/estado")
      setMundo(resposta.data.mapa);
      setTotalEntidades(resposta.data.total_entidades);
      setHorasMundo(resposta.data.horas_passadas)
      setAlerta(null)
    }
    catch(erro){
      setAlerta("O estado do mundo não pode ser atualizado, por favor confira sua conexão.");
    }
  };

  const iniciarSimulacao = async () => {
    try{
      await axios.post("http://127.0.0.1:8000/iniciar", { tamanho_mapa: tamMapa });
      carregarEstado(); 

    }catch(error){
      setAlerta("O mundo não pode ser iniciado, por favor confira sua conexão.");
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

  // roda toda vez que a pagina recarregar
  useEffect(() => {
    carregarEstado();
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
          quantTick={quantTick} 
          setQuantTick={setQuantTick} 
          tamMapa={tamMapa}
          setTamMapa={setTamMapa}
        />


        {/* funciona como um if na estrutura {variavel && (HTML)} */}
        {alerta && (<div className=" mt-3 alert alert-warning text-center fw-bold">{alerta}</div>)}

      </div>
    </>
    )};

export default App