# @modelo de dados - Telefonia Voz

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class Cliente(BaseModel):
    idCliente: int
    noCliente: str 
    dtCadastro: Optional[datetime] = None
    tpPessoa: str # Pessoa Fisica F ou Pessoa Jurídica J
    nuCPFCNPJ: int
    cdSituacao: int # 1 - Ativo, 2 - Inativo, 3 - Suspenso

external_data = {'idCliente': '123', 'noCliente': 'Sergio Vilela','dtCadastro': '2017-06-01 12:22', 'tpPessoa': 'F', 'nuCPFCNPJ': '61451835787', 'cdSituacao': 'A'}
cliente = Cliente(**external_data)

class Telefone(BaseModel):
    idTelefone: int
    nuTelefone: int
    idCliente: int
    dtAtivacao: datetime
    dtDesativacao: Optional[datetime] = None
    tpTelefone: str # Fixo F, Movel M, Especial E, 0800 8
    cdSituacao: int # 1 - Ativo, 2 - Inativo, 3 - Suspenso
    idPlano: int

external_data = {'idTelefone': '1', 'nuTelefone': '5521982149680', 'idCliente': '123', 'dtAtivacao': '2017-06-01 12:22', 'tpTelefone': 'M', 'cdSituacao': 'A'}
telefone= Telefone(**external_data)
external_data = {'idTelefone': '2', 'nuTelefone': '5521982149683', 'idCliente': '123', 'dtAtivacao': '2017-06-01 12:22', 'tpTelefone': 'M', 'cdSituacao': 'A'}
telefone= Telefone(**external_data)

class Plano(BaseModel):
    idPlano: int
    tpTelefone: str # Fixo F, Movel M, Especial E, 0800 8
    cdSituacao: int # 1 - Ativo, 2 - Inativo, 3 - Suspenso
    dtAtivacao: datetime
    dtDesativacao: Optional[datetime] = None
    qtDuracao: int # Em segundos
    vlDuracao: float # Valor da duracao
    qtMinimaInicial: int # Quantidade de segundos mínima para cobrança


external_data = {'idPlano': '123', 'tpTelefone': 'M', 'cdSituacao': 'A', 'dtAtivacao': '2017-06-01 12:22', 'qtDuracao': '60', 'vlDuracao': '0.50', 'qtMinimaInicial': '30'}
plano= Plano(**external_data)

class Chamada(BaseModel):
    idChamada: int
    nuTelefoneOrigem: int
    tpTelefoneOrigem: str # Fixo F, Movel M, Especial E, 0800 8
    CdOperadoraOrigem: int
    nuTelefoneDestino: int
    tpTelefoneDestino: str # Fixo F, Movel M, Especial E, 0800 8
    CdOperadoraDestino: int
    inChamadaACobrar: bool
    dtChamada: datetime
    qtDuracao: int
    vlChamada: float
    


external_data = {'idChamada': '1234', 'nuTelefoneOrigem': '5521982149680', 'tpTelefoneOrigem': 'M', 'CdOperadoraOrigem': '1', 
                 'nuTelefoneDestino': '5521982149680', 'tpTelefoneDestino': 'M', 'CdOperadoraDestino': '1', 'inChamadaACobrar': 'FALSE', 
                 'dtChamada': '2017-06-01 12:22', 'qtDuracao': '600', 'vlChamada': '5'}
chamada= Chamada(**external_data)
