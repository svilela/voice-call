# @modelo de dados - Telefonia Voz

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class Customer(BaseModel):
    customer_id: int
    customer_name: str 
    register_date: Optional[datetime] = None
    person_type: int # 1-Pessoa Fisica (Natural Person), 2-Pessoa Jurídica (Legal Person)
    natural_legal_id: int # CPF (EIN) ou CNPJ (TIN) do cliente
    customer_status_code: int # 1 - Active, 2 - Inactive, 3 - Suspended

external_data = {'customer_id': '123', 'customer_name': 'Sergio Vilela','register_date': '2017-06-01 12:22', 
                 'person_type': '1', 'natural_legal_id': '61451835787', 'customer_status_code': '1'}
customer = Customer(**external_data)

class Phone(BaseModel):
    phone_id: int
    phone_number: int
    customer_id: int
    activation_date: datetime
    deactivation_date: Optional[datetime] = None
    phone_type: str # Fixo F, Movel M, Especial E, 0800 8
    phone_status_code: int # 1 - Ativo, 2 - Inativo, 3 - Suspenso
    plan_id: int

external_data = {'phone_id': '1', 'phone_number': '5521982149680', 'customer_id': '123', 'activation_date': '2017-06-01 12:22', 
                 'phone_type': 'M', 'phone_status_code': 'A', 'plan_id': '123'}
phone = phone(**external_data)
external_data = {'phone_id': '1', 'phone_number': '5521982149683', 'customer_id': '123', 'activation_date': '2017-06-01 12:22', 
                 'phone_type': 'M', 'phone_status_code': 'A', 'plan_id': '123'}
phone = phone(**external_data)

class Plan(BaseModel):
    plan_id: int
    plan_status_code: int # 1 - Ativo, 2 - Inativo, 3 - Suspenso
    activation_date: datetime
    deactivation_date: Optional[datetime] = None


external_data = {'plan_id': '123', 'phone_type': 'M', 'plan_status_code': 'A', 'activation_date': '2017-06-01 12:22', 
                 'duration_time': '60', 'duration_value': '0.50', 'min_starting_time': '30'}
plan = Plan(**external_data)

class Price(BaseModel):
    plan_id: int
    customer_phone_type: str # Fixo F, Movel M, Especial E, 0800 8
    other_phone_type: str # Fixo F, Movel M, Especial E, 0800 8
    activation_date: datetime
    deactivation_date: Optional[datetime] = None
    duration_time: int # Em segundos
    duration_value: float # Valor da duracao
    min_starting_time: int # Quantidade de segundos mínima para cobrança


external_data = {'plan_id': '123', 'customer_phone_type': 'M', 'other_phone_type': 'M', 'activation_date': '2017-06-01 12:22', 
                 'duration_time': '60', 'duration_value': '0.50', 'min_starting_time': '5'}
price = Price(**external_data)

class Call_data_record(BaseModel):
    call_id: int
    phone_number_from: int
    phone_type_from: str # Fixo F, Movel M, Especial E, 0800 8
    operator_code_from: int
    phone_number_to: int
    phone_type_to: str # Fixo F, Movel M, Especial E, 0800 8
    operator_code_to: int
    call_collect_flag: bool
    call_date: datetime
    duration_time: int
    call_value: float
    


external_data = {'call_id': '1234', 'phone_number_from': '5521982149680', 'phone_type_from': 'M', 'operator_code_from': '1', 
                 'phone_number_to': '5521982149680', 'phone_type_to': 'M', 'operator_code_to': '1', 'call_collect_flag': 'FALSE', 
                 'call_date': '2017-06-01 12:22', 'duration_time': '600', 'call_value': '5'}
call_data_record = Call_data_record(**external_data)
