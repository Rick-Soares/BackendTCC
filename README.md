# 🚨 Sistema de Detecção de Quedas (Backend)

API desenvolvida em **Python + FastAPI** para um sistema de detecção de quedas utilizando IoT. O projeto faz parte de um TCC e é responsável pelo gerenciamento de usuários, dispositivos, contatos de emergência e alertas enviados pelo dispositivo.

## ✨ Funcionalidades

- Cadastro e autenticação de usuários
- Cadastro de dispositivos
- Cadastro de contatos de emergência
- Registro de alertas
- API REST para integração com ESP32
- Estrutura organizada em rotas, serviços e repositórios

## 🛠️ Tecnologias

- Python
- FastAPI
- SQLite
- JWT
- Pydantic
- Uvicorn

## 📂 Estrutura

```text
auth/
database/
models/
repositories/
routes/
services/
main.py
```

## 🚀 Como usar

### 1. Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd BackendTCC
```

### 2. Crie um ambiente virtual

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto e defina as variáveis necessárias.

Exemplo:

```env
SECRET_KEY=sua_chave123
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

### 5. Execute a aplicação

```bash
uvicorn main:app --reload
```

A API estará disponível em:

```
http://127.0.0.1:8000
```

## 📖 Documentação

Após iniciar a aplicação, acesse:

- Swagger: `http://127.0.0.1:8000/docs`

## 📌 Status

O projeto está em desenvolvimento. As próximas etapas incluem:

- Integração completa com ESP32
- Chamadas automáticas via Twilio
- Melhorias na segurança
- Expansão das funcionalidades da API
- Implementação de testes automatizados

## 👨‍💻 Autor

Desenvolvido por **Ricardo Soares** como projeto de TCC, aplicando conceitos de **Backend, APIs REST e Internet das Coisas (IoT)**.