"""
FastAPI Application - Currículo Moises Cardoso
"""
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import os
from pathlib import Path

from api.data import get_profile, get_experience, get_skills, get_contact

# Configuração de paths
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"

# Criar diretórios se não existirem
STATIC_DIR.mkdir(exist_ok=True)
TEMPLATES_DIR.mkdir(exist_ok=True)

# Inicializar FastAPI
app = FastAPI(
    title="Moises Cardoso - Currículo",
    description="API REST do currículo profissional de Moises Cardoso",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar arquivos estáticos
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# Configurar templates
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """
    Página principal com o currículo em HTML
    """
    profile_data = get_profile()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "profile": profile_data}
    )


@app.get("/api/profile")
async def api_profile():
    """
    Retorna dados completos do perfil em JSON

    Returns:
        dict: Dados completos do perfil profissional
    """
    return get_profile()


@app.get("/api/experience")
async def api_experience():
    """
    Retorna experiências profissionais em JSON

    Returns:
        dict: Lista de experiências profissionais
    """
    return get_experience()


@app.get("/api/skills")
async def api_skills():
    """
    Retorna habilidades e competências em JSON

    Returns:
        dict: Habilidades técnicas e certificações
    """
    return get_skills()


@app.get("/api/contact")
async def api_contact():
    """
    Retorna informações de contato em JSON

    Returns:
        dict: Informações de contato
    """
    return get_contact()


@app.get("/cv/download")
async def download_cv():
    """
    Download do currículo em PDF

    Returns:
        FileResponse: Arquivo PDF do currículo
    """
    pdf_path = STATIC_DIR / "mcardoso.pdf"
    if pdf_path.exists():
        return FileResponse(
            path=str(pdf_path),
            filename="mcardoso.pdf",
            media_type="application/pdf"
        )
    return {"error": "PDF não encontrado"}


@app.get("/health")
async def health_check():
    """
    Endpoint de health check

    Returns:
        dict: Status da aplicação
    """
    return {
        "status": "healthy",
        "service": "Moises Cardoso CV API",
        "version": "1.0.0"
    }


# Para execução local
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
