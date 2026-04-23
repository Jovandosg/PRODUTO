from __future__ import annotations
from abc import ABC, abstractclassmethod
from typing import List, Optional

from src.models.produto import Produto


class ProdutoRepositoryBase(ABC):

    """" Contrato para implementação de produtos"""

    @abstractmethods
    def listar(self) -> List[Produto]:
        raise NotImplementedError
    
    @abstractmethods
    def obter_por_id(self, id: int) -> Optional[Produto]:
        raise NotImplementedError
    
    @abstractmethods
    def criar(self, nome: str, preco: float, ativo: bool) -> Produto:
        raise NotImplementedError
    
    @abstractmethods
    def atualizar(self, id: int, nome: str, preco: float, ativo: bool) -> Optional[Produto]:
        raise NotImplementedError
    
    @abstractmethods
    def deletar(self, id: int) -> bool:
        raise NotImplementedError
