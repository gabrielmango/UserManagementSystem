# User Management System

## 🇺🇸 English

### 📚 Overview

**User Management System** is a robust FastAPI-based API providing authentication and authorization with three hierarchical levels (Manager, Admin, General User). The project follows DDT (Test-Driven Development) principles and clean architecture, making it ideal as a foundation for more complex systems.

### ✨ Key Features

- ✅ JWT Authentication
- ✅ 3-tier access hierarchy
- ✅ Complete user CRUD
- ✅ Granular permission control
- ✅ Ready for extension (e.g., e-commerce, SaaS)
- ✅ 100% test coverage

### 🛠️ Tech Stack

| Layer           | Technologies                         |
|-----------------|--------------------------------------|
| Framework       | FastAPI                              |
| Database        | SQLite (dev) / PostgreSQL (prd)     |
| ORM             | SQLAlchemy 2.0                       |
| Authentication  | JWT (OAuth2)                         |
| Testing         | Pytest + HTTPX                      |
| Dependencies    | Poetry                               |

### 🚀 Local Setup

```bash
# 1. Clone repository
git clone https://github.com/gabrielmango/UserManagementSystem.git

# 2. Setup environment
cd user-management-system
cp .env.example .env

# 3. Install dependencies
poetry install

# 4. Start server
poetry run uvicorn app.main:app --reload
```

Interactive docs available at: http://localhost:8000/docs

---

## 🇧🇷 Português

### 📚 Visão Geral

**User Management System** é uma API robusta desenvolvida com FastAPI que fornece autenticação e autorização com três níveis hierárquicos (Gerente, Administrador e Usuário Geral). O projeto segue princípios de DDT (Desenvolvimento Dirigido por Testes) e arquitetura limpa, sendo ideal para servir como base para sistemas mais complexos.

### ✨ Funcionalidades

- ✅ Autenticação via JWT
- ✅ Hierarquia de 3 níveis de acesso
- ✅ CRUD completo de usuários
- ✅ Controle de permissões granular
- ✅ Pronto para extensão (ex: e-commerce, SaaS)
- ✅ 100% cobertura de testes

### 🛠️ Stack Tecnológica

| Camada          | Tecnologias                          |
|-----------------|--------------------------------------|
| Framework       | FastAPI                              |
| Banco de Dados  | SQLite (dev) / PostgreSQL (prd)     |
| ORM             | SQLAlchemy 2.0                       |
| Autenticação    | JWT (OAuth2)                         |
| Testes          | Pytest + HTTPX                      |
| Dependências    | Poetry                               |

### 🚀 Executando Localmente

```bash
# 1. Clone o repositório
git clone https://github.com/gabrielmango/UserManagementSystem.git

# 2. Configure o ambiente
cd user-management-system
cp .env.example .env

# 3. Instale as dependências
poetry install

# 4. Inicie o servidor
poetry run uvicorn app.main:app --reload
```

Acesse a documentação interativa em: http://localhost:8000/docs

---

**📌 Nota/Note:**  
O sistema inclui um script para criar o primeiro usuário administrador:  
`poetry run python -m scripts.create_first_user admin@example.com senha123`  
The system includes a script to create the first admin user:  
`poetry run python -m scripts.create_first_user admin@example.com password123`

This version maintains technical accuracy while being more concise and visually appealing with badges and markdown formatting. The parallel structure makes it easy to read in both languages.