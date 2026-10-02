
export function Controle({iniciarSimu , avancarTurno}){
    return(
        <div className="container-fluid">

            <div className="row mt-5">
                <div className="col">
                    <button className="btn btn-success" onClick={iniciarSimu}>Iniciar novo mundo</button>
                </div>
                <div className="col">
                    <button className="btn btn-primary" onClick={avancarTurno}>Avançar turno</button>
                </div>
            </div>

        </div>
    )
    
}
