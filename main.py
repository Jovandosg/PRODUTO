#!/usr/bin/env python3

class Produto:
    """
    Docstring for Produto
    """

    def __init__(self, nome: str, preco: float):
        self.nome: str = nome
        self.preco: float = preco  # simples, sem property

    def __str__(self):
        return f"O produto é {self.nome} e o preco é {self.preco}"


# Crie a instância FORA do bloco da classe
p1 = Produto('Livro', 10.0)
print(p1)
