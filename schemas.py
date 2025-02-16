from pydantic import BaseModel, EmailStr, ConfigDict
from typing import List

                #Uma classe que pode ser usada como base para as outras
class ObrigacaoAcessoriaBase(BaseModel):
    nome: str
    periodicidade: str

                #Uma classe que herda de ObrigacaoAcessoriaBase sem diferenças
                #Usada pra diferenciar o momento de criação da empresa
class ObrigacaoAcessoriaCreate(ObrigacaoAcessoriaBase):
    pass

                #Herda de ObrigacaoAcessoriaBase e adiciona novos campos, sendo o Id e o Id da empresa
class ObrigacaoAcessoria(ObrigacaoAcessoriaBase):
    id: int

                #Permite que seja convertido de um objeto SQLAlchemy direto pra um objeto Pydantic
    model_config = ConfigDict(from_attributes=True)


class ObrigacaoAcessoriaUpdate(ObrigacaoAcessoriaBase):
    pass

class EmpresaBase(BaseModel):
    nome: str
    cnpj: str
    endereco: str
    email: EmailStr
    telefone: str

class EmpresaCreate(EmpresaBase):
    pass

class EmpresaUpdate(EmpresaBase):
    pass

class Empresa(BaseModel):
    id: int
    nome: str
    telefone: str
    endereco: str

    model_config = ConfigDict(from_attributes=True)


class Empresa(EmpresaBase):
    id: int

                #Uma empresa pode ter várias obrigações, se não tiver nenhuma o valor padrão é vazio
    obrigacoes: List[ObrigacaoAcessoria] = []

    model_config = ConfigDict(from_attributes=True)
