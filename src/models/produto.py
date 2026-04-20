#!/usr/bin/env python3
from __future__ import annotations

class Produto:
    """
    Docstring for Produto
    """

    def __init__(self, id_:int, nome:str, preco:float, ativo:bool = True) -> None:
        self._id: int = id_
        self.nome: str = nome
        self._preco:float = 0.0
        self.preco:float = preco 
        self.ativo:bool = ativo
    
    def __str__(self) -> str:
        return f"Produto(id={self._id}, nome={self.nome}, preço={self._preco}, ativo = {self.ativo})"
    
    @property
    def id(self)->int:
        return self._id
    
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, valor:float) -> None:
        if valor < 0:
            raise ValueError("O preço não pode ser negativo")
        self._preco = valor

    def aplicar_desconto(self, percentual:float) -> None:
        if not (0 <= percentual <= 100):
            raise ValueError("Percentual deve ser entre 0 e 100")
        desconto = self._preco * (percentual / 100)
        self._preco = desconto
    
    def ativar(self)->None:
        self.ativo = True

    def desativar(self) -> None:
        self.ativo = False 