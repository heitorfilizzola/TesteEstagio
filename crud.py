from sqlalchemy.orm import Session
import models
import schemas
from models import Empresa
from models import ObrigacaoAcessoria

                            #empresa : schemas.EmpresaCreate são os dados da empresa que será criada, validado pelo Pydantic
def criar_empresa(db: Session, empresa: schemas.EmpresaCreate):
    nova_empresa = models.Empresa(**empresa.model_dump())
    db.add(nova_empresa)
    db.commit()
    db.refresh(nova_empresa)
    return nova_empresa

def obter_empresa(db: Session, empresa_id: int):
    return db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()

def listar_empresas(db: Session):
    return db.query(models.Empresa).all()

def atualizar_empresa(db: Session, empresa: Empresa, novos_dados: schemas.EmpresaUpdate):
    for key, value in novos_dados.model_dump(exclude_unset=True).items():
        setattr(empresa, key, value)
    db.commit()
    db.refresh(empresa)
    return empresa

def apagar_empresa(db: Session, empresa_id:int):
    db.query(models.Empresa).filter(models.Empresa.id == empresa_id).delete()
    db.commit()
    return


def criar_obrigacao(db: Session, obrigacao: schemas.ObrigacaoAcessoriaCreate, empresa_id: int):
                            #Transforma a obrigação em um dictionary e associa a obrigacao a empresa
    nova_obrigacao = models.ObrigacaoAcessoria(**obrigacao.model_dump(), empresa_id=empresa_id)
    db.add(nova_obrigacao)
    db.commit()
    db.refresh(nova_obrigacao)
    return nova_obrigacao


def obter_obrigacao(db: Session, obrigacao_id: int):
    return db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.id == obrigacao_id).first()



def apagar_obrigacao(db: Session, obrigacao_id:int):
    obrigacao = db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.id == obrigacao_id).first()
    if obrigacao:
        db.delete(obrigacao)
        db.commit()
        return True
    return False

def atualizar_obrigacao(db: Session, obrigacaoacessoria: ObrigacaoAcessoria, novos_dados: schemas.ObrigacaoAcessoriaUpdate):
    for key, value in novos_dados.model_dump(exclude_unset=True).items():
        setattr(obrigacaoacessoria, key, value)
    db.commit()
    db.refresh(obrigacaoacessoria)
    return obrigacaoacessoria

def listar_obrigacoes(db: Session):
    return db.query(models.ObrigacaoAcessoria).all()
