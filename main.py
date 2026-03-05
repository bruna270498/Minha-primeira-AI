import os
import vertexai
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pydantic import BaseModel
from vertexai.generative_models import GenerativeModel
from fastapi.responses import FileResponse

# --- CONFIGURAÇÃO DO BACKEND (FastAPI) ---
# O FastAPI cria os "endpoints" (rotas) para que o seu site
# ou aplicativo consiga conversar com este script Python.
app = FastAPI()
load_dotenv()

#Configurando para que meu front tenha acesso a minha ai
app.add_middleware(
    CORSMiddleware,
    #cors atualmente está deixando qualquer front acessar mas quando crescer mudar para permitir só o seu
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

PROJECT_ID= os.getenv('PROJECT_ID')
LOCATION = os.getenv('LOCATION')

#Está sendo iniciado minha VERTEX 
vertexai.init(project=PROJECT_ID, location=LOCATION)
# Escolhi o modelo Gemini 1.5 Flash (rápido e barato/gratuito para testes)
model=GenerativeModel("gemini-2.5-flash")

#Essa linha de código é o "segurança da balada" da sua API. Ela usa uma biblioteca 
#chamada Pydantic (que o FastAPI ama) para garantir que os dados que chegam do mundo 
# exterior estejam no formato correto.
#Está class está criando um modelo de dados que define oque recebo
#BASEMODEL indica que minha class herda os "superpoderes" do Pydantic.
class PromptRequest(BaseModel):
    prompt: str
    
@app.get("/")
def ler_index():
    return FileResponse("index.html") # Coloque o nome do seu arquivo HTML aqui

#Aqui é a rota que será chamado pelo Front
@app.post("/chat")
async def gerar_resposta(request: PromptRequest):
    try:
        #Irei chamar a IA do Google e enviar o prompt
        print(request.prompt)
        response= model.generate_content(request.prompt)
        texto_final = response.text if response.text else "IA não gerou texto (pode ter sido bloqueado)"
        print(f">>> Resposta do Gemini:")
        return {"resposta":response.text}
    except Exception as e:
        return {"erro":str(e)}