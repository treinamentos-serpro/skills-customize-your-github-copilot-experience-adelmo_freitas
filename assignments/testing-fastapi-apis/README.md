# 📘 Atividade: Testando APIs com pytest

## 🎯 Objetivo

Pratique testes automatizados para APIs FastAPI usando pytest e TestClient, verificando respostas, dados retornados e códigos HTTP para cenários de sucesso e erro.

## 📝 Tarefas

### 🛠️ Testar consultas da API

#### Descrição
Use o código inicial, que contém uma API de livros e funções de teste com verificações incompletas. Complete os testes para consultar a coleção e buscar um livro específico.

Instale as dependências e execute os testes com:

```bash
python -m pip install fastapi httpx pytest
pytest starter-code.py -v
```

#### Requisitos
O programa concluído deve:

- Verificar que `GET /books` retorna o código `200` e uma lista com os livros cadastrados.
- Verificar que `GET /books/1` retorna o código `200` e os dados do livro com identificador `1`.
- Verificar que a busca por um identificador inexistente retorna `404`.

### 🛠️ Testar cadastro e validação

#### Descrição
Complete os testes para o cadastro de livros, incluindo uma requisição válida e outra com dados obrigatórios ausentes.

#### Requisitos
O programa concluído deve:

- Verificar que `POST /books` retorna `201` e o livro criado com um identificador.
- Verificar que uma requisição sem o campo obrigatório `author` retorna `422`.
- Usar asserções sobre o código HTTP e o conteúdo JSON das respostas.

### 🛠️ Testar atualização e remoção

#### Descrição
Complete os testes das operações de atualização e remoção e verifique também o comportamento quando o livro não existe.

#### Requisitos
O programa concluído deve:

- Verificar que `PUT /books/1` retorna `200` e os dados atualizados.
- Verificar que `DELETE /books/1` retorna `204` e que o livro não pode mais ser consultado.
- Verificar que atualizar ou remover um identificador inexistente retorna `404`.