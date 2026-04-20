from __future__ import annotations
from abc import ABC, abstractclassmethod
from typing import List, Optional

from src.models.produto import Produto


class ProdutoRepositoryBase(ABC):

    """" Contrato para implementação de produtos"""

    @abstractmethods
    def listar(self) -> List
