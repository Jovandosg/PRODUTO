from __future__ import annotations
from typing import List,Optional

from sqlalchemy.orm import Session

from src.models.produto import Produto
from src.models.produto_db import ProdutoDB
from src.services.produto_repo_base import ProdutoRepositoryBase

class ProdutoRepositorySQLAlchemy(ProdutoRepositoryBase):
    """Implementação do REPO utilizando SQLALchemy + SQLite"""

    def __init__(self, db:Session):
        self._db = db

    def _db_to_entity(self, produto_db: ProdutoDB) -> Produto:
        """ Converter modelo ORM para a entidade Produto"""
        return Produto(
            id_ = produto_db.id,
            nome= produto_db.nome,
            preco = produto_db.preco,
            ativo = produto_db.ativo
        )
    
    def listar(self) -> List[Produto]:
        produtos_db = self._db.query(ProdutoDB).all()
        #select * from produtos
        return [self._db_to_entity(p) for p in produtos_db] 
    
    def buscar_por_id(self, id_:int) -> Optional[Produto]:
        produtos_db = self._db.query(ProdutoDB).filter(ProdutoDB.id == id_).first()
        #select * from produtos where id = {_id}

        if not produtos_db:
            return None
        return self._db_to_entity(produtos_db)

    def criar(self, nome:str, preco:float, ativo:bool = True) -> Produto:
        produto_db = ProdutoDB(nome=nome, preco=preco, ativo=ativo)

        self._db.add(produto_db)

        #INSERT INTO produtos (nome, preco, ativo) values ("Caderno", 10.5, True)
        self._db.commit()  
        self._db.refresh(produto_db)

        return self._db_to_entity(produto_db=produto_db)
    
    def atualizar(self, id_:int, nome:str, preco:float, ativo:bool) -> Optional[Produto]:
        produto_db = self._db.query(ProdutoDB).filter(ProdutoDB.id == id_).first()
        if not produto_db:
            return None
        
        produto_db.nome = nome
        produto_db.preco = preco
        produto_db.ativo = ativo

        #Update produtos set nome= "Lapis", preco=1.00, ativo = True where id=id_ 
        self._db.commit()
        self._db.refresh(produto_db)

        return self._db_to_entity(produto_db)
    
    def remover(self, id_:int) -> bool:
        produto_db = self._db.query(ProdutoDB).filter(ProdutoDB.id == id_).first()
        #select * from produtos where id=id_

        if not produto_db:
            return False
        
        self._db.delete(produto_db)
        
        #delete from produtos where id=id_
        self._db.commit()
        
        return True
 