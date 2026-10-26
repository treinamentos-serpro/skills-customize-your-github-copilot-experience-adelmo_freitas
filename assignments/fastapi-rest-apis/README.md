# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar um catálogo de livros, praticando rotas HTTP, validação de dados com Pydantic e respostas com códigos de status apropriados.

## 📝 Tarefas

### 🛠️ Criar operações de leitura e cadastro

#### Descrição
Complete o código inicial para criar uma API FastAPI que permita consultar livros e cadastrar novos livros. Os dados devem ficar em memória enquanto a aplicação estiver em execução.

#### Requisitos
O programa concluído deve:

- Criar a aplicação FastAPI e um modelo Pydantic para os dados do livro, com título, autor e ano de publicação.
- Implementar `GET /books` para listar os livros cadastrados.
- Implementar `GET /books/{book_id}` para buscar um livro pelo identificador e responder com `404` quando ele não existir.
- Implementar `POST /books` para cadastrar um livro, gerar seu identificador e responder com o código `201`.
- Permitir testar as rotas pela documentação interativa em `/docs`.

Para executar localmente, instale as dependências e inicie o servidor:

```bash
python -m pip install fastapi uvicorn
uvicorn starter-code:app --reload
```

### 🛠️ Implementar atualização e remoção

#### Descrição
Adicione as operações necessárias para atualizar ou remover um livro existente. Use o identificador da rota para localizar o recurso e trate os casos em que ele não existe.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /books/{book_id}` para substituir os dados de um livro existente.
- Implementar `DELETE /books/{book_id}` para remover um livro existente e responder com o código `204`.
- Responder com `404` nas operações de atualização e remoção quando o identificador não corresponder a um livro cadastrado.
- Confirmar, usando `/docs`, que as operações criam, consultam, atualizam e removem livros como esperado.