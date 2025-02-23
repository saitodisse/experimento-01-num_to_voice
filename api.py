import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from num_to_voice import converter_numero_para_palavras

# Carrega as variáveis de ambiente
load_dotenv()

app = FastAPI(
    title="Conversor de Números para Extenso",
    description="API para converter números em sua forma extensa em português",
    version="1.0.0"
)

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, você deve especificar os domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar os arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return FileResponse("static/index.html")

@app.get("/health")
async def health_check():
    """Endpoint para verificação de saúde da API"""
    return {"status": "healthy"}

@app.get("/converter/{numero}")
async def converter_numero(numero: int):
    try:
        resultado = converter_numero_para_palavras(numero)
        return {"extenso": resultado}
    except ValueError as e:
        raise HTTPException(status_code=400, detail={"error": str(e)})

if __name__ == "__main__":
    import uvicorn
    
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    
    uvicorn.run(
        "api:app",
        host=host,
        port=port,
        reload=False,  # Desabilita reload em produção
        workers=4  # Número de workers para melhor performance
    ) 