from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models import ProdutoDB
from schemas import ProdutoCreate, ProdutoResponse
from models import FilmesDB
from schemas import FilmesCreate, FilmesResponse

from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.on_event("startup") #o decorator se baseia em um eveto (tipo js) no caso a startup 
def criar_tabelas():
    Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    # em produção, restringir para o domínio real do front-end
    allow_methods=['*'],
    allow_headers=['*'],
)

# GET /produtos/{id} -> retorna todos os produtos
@app.get('/produtos', response_model=list[ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(ProdutoDB).all()

# GET /produtos/{id} -> retorna um único produto pelo id
@app.get('/produtos/{produto_id}', response_model=ProdutoResponse)
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
    if produto is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    return produto

@app.post('/produtos', response_model=ProdutoResponse, status_code=201)
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    novo_produto = ProdutoDB(**produto.dict()) 
    db.add(novo_produto) #insert into 
    db.commit()
    db.refresh(novo_produto)
    return novo_produto

# DELETE /produtos/{id} -> remove um produto do banco de dados
@app.delete('/produtos/{produto_id}', status_code=204)
def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
    if produto is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    db.delete(produto)
    db.commit()
    return ('Produto deletado com sucesso')

# PUT /produtos/{id} -> atualiza um produto existente no banco
@app.put('/produtos/{produto_id}', response_model=ProdutoResponse)
def atualizar_produto(produto_id: int, dados: ProdutoCreate, db: Session = Depends(get_db)):
    produto = db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
    if produto is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    produto.nome = dados.nome
    produto.preco = dados.preco
    produto.quantidade = dados.quantidade
    db.commit()
    db.refresh(produto)
    return produto    


#FILMESSSSS

# GET  -> retorna todos os produtos
@app.get('/filmes_nacionais', response_model=list[FilmesResponse])
def listar_filmes(db: Session = Depends(get_db)):
    return db.query(FilmesDB).all()


# GET -> retorna um único produto pelo id
@app.get('/filmes_nacionais/{produto_id}', response_model=FilmesResponse)
def obter_filme(filmes_nacionais_id: int, db: Session = Depends(get_db)):
    filmes_nacionais = db.query(FilmesDB).filter(FilmesDB.id == filmes_nacionais_id).first()
    if filmes_nacionais is None:
        raise HTTPException(status_code=404, detail='Filme não encontrado')
    return filmes_nacionais

#POST
@app.post('/filmes_nacionais', response_model=FilmesResponse, status_code=201)
def criar_filme(filmes_nacionais: FilmesCreate, db: Session = Depends(get_db)):
    novo_filme = FilmesDB(**filmes_nacionais.dict()) 
    db.add(novo_filme) #insert into 
    db.commit()
    db.refresh(novo_filme)
    return novo_filme

# DELETE -> remove um produto do banco de dados
@app.delete('/filmes_nacionais/{filmes_nacionais_id}', status_code=204)
def remover_filme(filmes_nacionais_id: int, db: Session = Depends(get_db)):
    filmes_nacionais = db.query(FilmesDB).filter(FilmesDB.id == filmes_nacionais_id).first()
    if filmes_nacionais is None:
        raise HTTPException(status_code=404, detail='Filme não encontrado')
    db.delete(filmes_nacionais)
    db.commit()
    return HTTPException(status_code=204, detail='Filme deletado com sucesso')

# PUT -> atualiza um produto existente no banco
@app.put('/filmes_nacionais/{filmes_nacionais_id}', response_model=FilmesResponse)
def atualizar_filme(filmes_nacionais_id: int, dados: FilmesCreate, db: Session = Depends(get_db)):
    filmes_nacionais = db.query(FilmesDB).filter(FilmesDB.id == filmes_nacionais_id).first()
    if filmes_nacionais is None:
        raise HTTPException(status_code=404, detail='Filme não encontrado')
    filmes_nacionais.titulo = dados.titulo
    filmes_nacionais.diretor = dados.diretor
    filmes_nacionais.genero = dados.genero
    filmes_nacionais.duracao_min = dados.duracao_min
    db.commit()
    db.refresh(filmes_nacionais)
    return filmes_nacionais    