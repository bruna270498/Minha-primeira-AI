# 🚀 Projeto Full Stack: Chat Agente Gemini 2.5 Flash

Este é um projeto completo de um **Chatbot de Inteligência Artificial** utilizando:

-  **Backend em Python (FastAPI)**
-  Integração com o modelo **Gemini 2.5 Flash**
-  API do **Google Vertex AI**
-  Frontend moderno em **HTML5 + JavaScript**
-  Suporte a renderização Markdown

---

# 📌 Pré-requisitos Obrigatórios

Antes de rodar o projeto, configure o ambiente Google Cloud na sua máquina.

## 1️⃣ Instalar o Google Cloud CLI

Instale o Google Cloud CLI:  
https://cloud.google.com/sdk/docs/install

---

## 2️⃣ Criar Projeto no GCP

Você precisa:

- Ter um **Project ID válido**
- Ativar a API **Vertex AI**

---

## 3️⃣ Autenticação

No terminal, execute:

```bash
# Login na sua conta Google
gcloud auth login

# Habilita Application Default Credentials (ADC)
gcloud auth application-default login

# Define o projeto padrão (recomendado)
gcloud config set project SEU_PROJECT_ID_AQUI
```

---

# Estrutura do Projeto

O projeto é dividido em duas partes principais:

---

## Backend (O Cérebro)

Arquivo principal: `main.py`

### Responsabilidades

- Receber perguntas via HTTP (POST)
- Validar dados com **Pydantic**
- Consultar a API do Vertex AI
- Tratar erros e filtros de segurança
- Configurar **CORS**
- Gerenciar variáveis de ambiente

### Tecnologias Backend

- FastAPI
- Uvicorn
- google-cloud-aiplatform
- python-dotenv
- Pydantic

---

##  Frontend (Interface)

Arquivo principal: `index.html`

### Responsabilidades

- Capturar a digitação do usuário
- Enviar requisições para `http://localhost:8000`
- Renderizar resposta da IA com **Marked.js**
- Manter scroll automático do chat

### Tecnologias Frontend

- Vanilla JavaScript (Fetch API)
- CSS3
- Marked.js (CDN)

---

#  Arquivos de Automação

O projeto possui dois arquivos `.bat` para facilitar execução e deploy.

---

##  rodar_local.bat

- Executa o projeto via Docker
- É necessário estar com o **Docker aberto**
- Basta dar **duplo clique**
- O container será iniciado automaticamente

---

##  deploy_nuvem.bat

- Realiza deploy para o Google Cloud Run
- Basta dar **duplo clique**
- O serviço será publicado na nuvem

### ⚠️ Antes de rodar o deploy

Você deve:

- Ter o Google Cloud CLI instalado
- Estar autenticado (`gcloud auth login`)
- Estar com o projeto configurado

---

#  Executando Manualmente (Sem Docker)

Dentro da pasta do projeto:

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate

# Instalar dependências
pip install fastapi uvicorn google-cloud-aiplatform python-dotenv pydantic

# Iniciar servidor
uvicorn main:app --reload
```

Servidor disponível em:

```
http://localhost:8000
```

---

#  Deploy Manual no Cloud Run

```bash
gcloud run deploy meu-app \
  --source . \
  --region us-central1 \
  --allow-unauthenticated \
  --memory 1024Mi
```

---

#  Remover Serviço da Nuvem (Evitar Custos)

Após testar, delete o serviço para não gerar cobranças:

```bash
gcloud run services delete meu-app --region us-central1
```

Se ocorrer erro de cache:

```bash
gcloud run deploy meu-app --source . --region us-central1 --allow-unauthenticated --memory 1024Mi
```

---

#  Observações Importantes

- Sempre delete o serviço após testes
- Verifique se o projeto correto está selecionado
- Mantenha suas credenciais seguras
- Utilize `.env` para variáveis sensíveis
- O Cloud Run pode gerar cobrança se o serviço permanecer ativo

---

#  Objetivo do Projeto

Este projeto demonstra:

- Integração real com IA generativa
- Arquitetura Full Stack moderna
- Deploy automatizado em nuvem
- Boas práticas com autenticação e segurança
- Uso profissional do ecossistema Google Cloud
- Organização para portfólio técnico

