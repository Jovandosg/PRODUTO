from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field

class ProdutoBase(BaseModel):
    nome: str = Field(..., min_length=3, max_length=100)
    preco: float = Field(..., gt=0 , lt=10000, description="Preço deve ser maior do que zero e menor do que 10.000")
    ativo: bool = True

class ProdutoCreate(ProdutoBase):
    """DTO para criação do produto (POST)"""
    pass

class ProdutoUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length=3, max_length=100)
    preco: Optional[float] = Field(None, gt=0 , lt=10000)
    ativo: Optional[bool] = None

class ProdutoRead(ProdutoBase):
    id: int

    class Config:
        from_attributes = True