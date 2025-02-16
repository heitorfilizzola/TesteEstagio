from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Empresa, ObrigacaoAcessoria
import schemas
import crud
from database import engine, Base, get_database

app = FastAPI()

Base.metadata.create_all(bind=engine)



@app.post("/empresas/", response_model=schemas.Empresa, status_code=201)
def criar_empresa(empresa: schemas.EmpresaCreate, db: Session = Depends(get_database)):
    return crud.criar_empresa(db, empresa)


@app.get("/empresas/{empresa_id}", response_model=schemas.Empresa)
def obter_empresa(empresa_id: int, db: Session = Depends(get_database)):
    empresa = crud.obter_empresa(db, empresa_id)

    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return empresa

@app.put("/empresas/{empresa_id}", response_model=schemas.Empresa)
def atualizar_empresa(empresa_id: int, empresa_atualizada: schemas.EmpresaUpdate, db: Session = Depends(get_database)):
    empresa = crud.obter_empresa(db, empresa_id)
    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")

    empresa_atualizada = crud.atualizar_empresa(db, empresa, empresa_atualizada)

    if not empresa_atualizada:
        raise HTTPException(status_code=500, detail="Erro ao atualizar a empresa")

    return empresa_atualizada


@app.get("/empresas/", response_model=list[schemas.Empresa])
def listar_empresas(db: Session = Depends(get_database)):
    listar = crud.listar_empresas(db)
    return listar


@app.delete("/empresas/{empresa_id}", status_code=204)
def apagar_empresa(empresa_id:int, db: Session = Depends(get_database)):
    empresa = crud.obter_empresa(db, empresa_id)
    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    crud.apagar_empresa(db, empresa_id)
    return {"message": "Empresa apagada com sucesso"}


@app.post("/empresas/{empresa_id}/obrigacoes/", response_model=schemas.ObrigacaoAcessoria, status_code=201)
def criar_obrigacao(
        empresa_id: int, obrigacao: schemas.ObrigacaoAcessoriaCreate, db: Session = Depends(get_database)
):
    empresa = crud.obter_empresa(db, empresa_id)
    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return crud.criar_obrigacao(db, obrigacao, empresa_id)



@app.get("/empresas/{empresa_id}/obrigacoes/{obrigacao_id}", response_model=schemas.ObrigacaoAcessoria)
def obter_obrigacao(obrigacao_id: int, empresa_id: int, db: Session = Depends(get_database)):
    empresa = crud.obter_empresa(db, empresa_id)

    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")

    obrigacao = crud.obter_obrigacao(db, obrigacao_id)
    if not obrigacao:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")
    return obrigacao


@app.delete("/empresas/{empresa_id}/obrigacoes/{obrigacao_id}")
def apagar_obrigacao(obrigacao_id:int, empresa_id:int, db: Session = Depends(get_database)):
    obrigacao = crud.obter_obrigacao(db, obrigacao_id)
    if not obrigacao:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")
    crud.apagar_obrigacao(db, obrigacao_id)
    return {"message": "Obrigação apagada com sucesso"}

@app.put("/empresas/{empresa_id}/obrigacoes/{obrigacao_id}", response_model=schemas.ObrigacaoAcessoria)
def atualizar_obrigacao(obrigacao_id: int, obrigacaoacessoria_atualizada: schemas.ObrigacaoAcessoriaUpdate, db: Session = Depends(get_database)):
    obrigacao = crud.obter_obrigacao(db, obrigacao_id)
    if not obrigacao:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")
    obrigacaoacessoria_atualizada = crud.atualizar_obrigacao(db, obrigacao, obrigacaoacessoria_atualizada)

    if not obrigacaoacessoria_atualizada:
        raise HTTPException(status_code=500, detail="Erro ao atualizar a Obrigacao")
    return obrigacaoacessoria_atualizada

@app.get("/obrigacoes/", response_model=list[schemas.ObrigacaoAcessoria], status_code=200)
def listar_obrigacoes( db: Session = Depends(get_database)):
    obrigacoes = crud.listar_obrigacoes(db)
    return obrigacoes


#uvicorn main:app --reload