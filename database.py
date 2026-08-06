# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Formato: mysql+pymysql://usuario:senha@host/nome_do_banco
DATABASE_URL = 'mysql+pymysql://root:@localhost/loja' #string de conexão: fala qual é o usuário, senha, nome do banco e onde esta o banco
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #cria a sessão 
Base = declarative_base() #para instanciar o obj Base para fazer qualquer coisa no banco

# Função de dependência: abre uma sessão por requisição e garante o fechamento
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()