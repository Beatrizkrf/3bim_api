# schemas.py
from pydantic import BaseModel

class ProdutoBase(BaseModel):
    nome: str
    preco: float
    quantidade: int

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoResponse(ProdutoBase):
    id: int

class Config:
    from_attributes = True


class FilmesBase(BaseModel):
    titulo: str
    diretor: str
    genero: str
    duracao_min: int

class FilmesCreate(FilmesBase):
    pass

class FilmesResponse(FilmesBase):
    id: int

