import { useState , useEffect, useRef} from 'react'
import axios from 'axios';
import {Controle } from './componentes/Controle'
import {Mapa} from './componentes/Mapa'

function App() {
  const [mundo , setMundo] = useState([]);
  const [totalEntidades , setTotalEntidades] = useState(0);
  const [alerta , setAlerta] = useState(null)

  const carregarEstado = async () => {
    try{
      const resposta = await axios.get("http://127.0.0.1:8000/estado")
      setMundo(resposta.data.mapa);
      setTotalEntidades(resposta.data.total_entidades);
      setAlerta(null)
    }
    catch(erro){
      setAlerta("O estado do mundo não pode ser atualizado, por favor confira sua conexão.");
    }
  };

  const iniciarSimulacao = async () => {
    try{
      await axios.post("http://127.0.0.1:8000/iniciar", { tamanho_mapa: 16 });
      carregarEstado(); 

    }catch(error){
      setAlerta("O mundo não pode ser iniciado, por favor confira sua conexão.");
    }
  };

  const avancarTurno = async () => {
    try{
      await axios.post("http://127.0.0.1:8000/tick", { tick: 1 });
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

  return (
    <>
      <div className='container-fluid p-3 '>

        <h1 className='display-3'>Projeto Terra</h1>
        <p className='lead mt-3'>Total de entidades:</p>
        <p>{totalEntidades}</p>

        <Controle iniciarSimu={iniciarSimulacao} avancarTurno={avancarTurno}/>
        {/* funciona como um if na estrutura {variavel && (HTML)} */}
        {alerta && (<div className=" mt-3 alert alert-warning text-center fw-bold">{alerta}</div>)}
        <Mapa mundo={mundo}/>

      </div>
    </>
    )};

export default App