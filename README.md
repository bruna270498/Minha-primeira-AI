# Projeto Full Stack: Chat Agente Gemini 2.5 Flash

Este é um projeto completo de um Chatbot de Inteligência Artificial.  
Ele utiliza um backend robusto em **Python (FastAPI)** para se conectar ao modelo **Gemini 2.5 Flash** através do **Google Vertex AI** e um frontend moderno e responsivo em **HTML5/JavaScript** com suporte a Markdown.

---

# 📌 Pré-requisitos Obrigatórios

Antes de rodar o projeto, você precisa configurar o ambiente do Google Cloud na sua máquina:

## 1️⃣ Instalar o Google Cloud CLI

Instale o Google Cloud CLI:  
https://cloud.google.com/sdk/docs/install

## 2️⃣ Criar Projeto no GCP

- Ter um **Project ID válido**
- Ativar a API **Vertex AI**

## 3️⃣ Autenticação

Abra o terminal e execute:

```bash
# Login na sua conta Google
gcloud auth login

# Habilita Application Default Credentials (ADC)
gcloud auth application-default login

# Define o projeto padrão (recomendado)
gcloud config set project SEU_PROJECT_ID_AQUI