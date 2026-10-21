from pydantic import BaseModel , field_validator

class AvancaTick(BaseModel):
    tick : int  
    
class IniciarMundo(BaseModel):
   # Tipado estritamente como int para o Pylance não reclamar
    tamanho_mapa: int = 16
    qtd_coelhos: int = 11  
    qtd_cobras: int = 9    
    qtd_gavioes: int = 5
    qtd_arvores: int = 10

    @field_validator("tamanho_mapa", mode="before")
    @classmethod
    def substituir_none(cls, valor):
        if valor is None:
            return 16
        return valor