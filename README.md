# 📦 API de Produtos

API RESTful para gerenciamento de produtos, construída com **FastAPI**, **SQLAlchemy** e **SQLite**, seguindo o padrão de arquitetura em camadas com separação entre modelos de domínio, ORM, schemas Pydantic e repositório.

---

## 🚀 Tecnologias

| Tecnologia | Versão |
|---|---|
| Python | 3.12+ |
| FastAPI | 0.115.0 |
| Uvicorn | 0.30.0 |
| Pydantic | 2.9.0 |
| SQLAlchemy | latest |
| SQLite | embutido |

---

## 📁 Estrutura do Projeto

```
PRODUTO/
├── main.py                        # Script de exemplo simples da classe Produto
├── requirements.txt               # Dependências do projeto
├── data/                          # Banco de dados SQLite gerado em runtime
├── src/
│   ├── models/
│   │   ├── produto.py             # Modelo de domínio (regras de negócio)
│   │   ├── produto_db.py          # Modelo ORM (mapeamento para banco de dados)
│   │   └── produto_schemas.py     # Schemas Pydantic (validação e serialização)
│   ├── services/
│   │   ├── produto_repo_base.py   # Contrato abstrato do repositório
│   │   └── produto_repo_sqlalchemy.py  # Implementação com SQLAlchemy
│   └── utils/
│       ├── database.py            # Configuração da engine e sessão SQLAlchemy
│       └── main.py                # Ponto de entrada da API (FastAPI app)
└── tests/                         # Testes automatizados
```

---

## ⚙️ Instalação e Execução

### 1. Clone o repositório

```bash
git clone https://github.com/Jovandosg/PRODUTO.git
cd PRODUTO
```

### 2. Crie e ative o ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Inicie a API

```bash
uvicorn src.utils.main:app --reload
```

A API estará disponível em: [http://localhost:8000](http://localhost:8000)

---

## 📖 Documentação Interativa

Após iniciar o servidor, acesse:

- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🔌 Endpoints

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/` | Healthcheck da API |
| `GET` | `/produtos` | Lista todos os produtos |
| `GET` | `/produtos/{id}` | Retorna um produto pelo ID |
| `POST` | `/produtos` | Cria um novo produto |
| `PUT` | `/produtos/{id}` | Atualiza um produto existente |

### Exemplo de payload (POST /produtos)

```json
{
  "nome": "Livro Python",
  "preco": 49.90,
  "ativo": true
}
```

### Exemplo de resposta

```json
{
  "id": 1,
  "nome": "Livro Python",
  "preco": 49.90,
  "ativo": true
}
```

---

## 🏗️ Arquitetura

O projeto segue separação de responsabilidades em camadas:

```
Requisição HTTP
      │
      ▼
  FastAPI (src/utils/main.py)
      │
      ▼
  ProdutoService  ◄──── regras de negócio
      │
      ▼
  ProdutoRepositoryBase (contrato abstrato)
      │
      ▼
  ProdutoRepositorySQLAlchemy (implementação concreta)
      │
      ▼
  SQLite via SQLAlchemy
```

**Modelos:**
- `Produto` — domínio puro com validações (preço não negativo, desconto, ativar/desativar)
- `ProdutoDB` — mapeamento ORM para a tabela `produtos`
- `ProdutoCreate / ProdutoUpdate / ProdutoRead` — schemas Pydantic para entrada e saída da API

---

## 🧪 Script de Exemplo

Para testar a classe de domínio isolada:

```bash
./main.py
# Saída: O produto é Livro e o preco é 10.0
```

---

## 📝 Licença

Este projeto está sob a licença MIT.
