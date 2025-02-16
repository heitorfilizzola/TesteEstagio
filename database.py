from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


if not DATABASE_URL:
    raise ValueError("DATABASE_URL não definido no arquivo .env")


engine = create_engine(DATABASE_URL)

Base = declarative_base()

                    # Cria sessão para interagir com o banco, definindo os commits automaticos para false em que so salva os dados quando se chama o .comit()
                    # o autoflush que evita erros consultando os dados antes de salvar
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



def get_database():
    db = SessionLocal() #Cria uma sessão local conectando com o banco de dados
                    #O sessionlocal é um sessionmaker criado e permite executar consultas e transações com o banco
    try:
        yield db    # Isso libera a sessão para o FastAPI
    finally:
        db.close()
