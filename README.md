# Projeto Full Stack: Chat Agente Gemini 2.5 Flash

Este é um projeto completo de um Chatbot de Inteligência Artificial. Ele utiliza um backend robusto em **Python (FastAPI)** para se conectar ao modelo **Gemini 2.5 Flash** do Google Vertex AI e um frontend moderno e responsivo em **HTML5/JS** com suporte a Markdown.


---
## Pré-requisitos Obrigatórios

Antes de rodar o projeto, você precisa configurar o ambiente do Google Cloud na sua máquina:

1. **Google Cloud CLI:** [Instale o gcloud CLI](https://cloud.google.com/sdk/docs/install) no seu computador.
2. **Projeto no GCP:** Tenha um ID de projeto válido com a API **Vertex AI** ativada.
3. **Autenticação:** Abra o terminal e rode os comandos abaixo para autorizar seu computador:

```bash
# Faz o login na sua conta Google
gcloud auth login

# Configura a autenticação para que as bibliotecas Python (ADC) funcionem
gcloud auth application-default login

# Define o projeto padrão (opcional, mas recomendado)
gcloud config set project SEU_PROJECT_ID_AQUI
```
---

## Estrutura do Projeto

O projeto é dividido em duas partes principais:

### 1. Backend (O Cérebro)
Localizado no arquivo `main.py`, ele é responsável por:
- Receber as perguntas do navegador via protocolo HTTP (POST).
- Validar os dados usando **Pydantic**.
- Consultar a API do **Google Vertex AI**.
- Tratar erros e filtros de segurança da IA.
- Liberar o acesso para o Frontend através do **CORS**.

### 2. Frontend (A Interface)
Localizado no arquivo `index.html`, ele é responsável por:
- Capturar a digitação do usuário.
- Enviar as requisições para o servidor local (`localhost:8000`).
- Renderizar a resposta da IA usando a biblioteca **Marked.js** (transformando símbolos como `**` e `*` em negrito e listas reais).
- Manter o scroll automático do chat.

---

## 🛠️ Tecnologias e Dependências

### Backend
- **FastAPI & Uvicorn**: Para o servidor web.
- **google-cloud-aiplatform**: SDK oficial do Google para o Gemini.
- **python-dotenv**: Para gerenciar chaves e IDs de projeto com segurança.

### Frontend
- **Vanilla JavaScript**: Lógica de comunicação (Fetch API).
- **CSS3**: Estilização de balões de chat e layout.
- **Marked.js (CDN)**: Conversor de Markdown para HTML.

---

## 🚀 Como Executar o Projeto

### Passo 1: Configurar o Backend
No terminal, dentro da pasta do projeto:

```bash
# Criar e ativar ambiente virtual
python -m venv venv
source venv/bin/activate  # (Linux/Mac) ou venv\Scripts\activate (Windows)

# Instalar dependências
pip install fastapi uvicorn google-cloud-aiplatform python-dotenv pydantic

# Iniciar o servidor
uvicorn main:app --reload