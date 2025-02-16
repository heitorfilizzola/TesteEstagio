from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Empresa(Base):
    __tablename__ = "Empresa"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cnpj = Column(String, unique=True, index=True)
    endereco = Column(String, index=True)
    email = Column(String)
    telefone = Column(String)

    obrigacoes = relationship("ObrigacaoAcessoria", back_populates="empresa")

class ObrigacaoAcessoria(Base):
    __tablename__ = "ObrigacaoAcessoria"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    periodicidade = Column(String, index=True)

    empresa_id = Column(Integer, ForeignKey("Empresa.id"))
    empresa = relationship("Empresa", back_populates="obrigacoes")

