# Moises Cardoso - Currículo Online

Projeto FastAPI para hospedar currículo profissional na Vercel.

## Sobre

Este projeto fornece uma API REST e uma interface web moderna para visualizar o currículo profissional de Moises Cardoso, desenvolvedor .NET Sênior especializado em Pagamentos & Adquirência.

## Tecnologias

- **Backend**: FastAPI (Python)
- **Frontend**: HTML5, CSS3, Jinja2 Templates
- **Hospedagem**: Vercel
- **Features**: API REST, Download de PDF, Design Responsivo

## Estrutura do Projeto

```
MoisesCardosoCV2025/
├── api/
│   ├── index.py          # FastAPI app principal
│   └── data.py           # Dados estruturados do currículo
├── static/
│   ├── style.css         # Estilos da página
│   └── mcardoso.pdf      # CV em PDF
├── templates/
│   └── index.html        # Template da página
├── requirements.txt      # Dependências Python
├── vercel.json          # Configuração Vercel
└── README.md            # Este arquivo
```

## Endpoints da API

- `GET /` - Página web com o currículo
- `GET /api/profile` - JSON com dados completos do perfil
- `GET /api/experience` - JSON com experiências profissionais
- `GET /api/skills` - JSON com competências técnicas
- `GET /api/contact` - JSON com informações de contato
- `GET /cv/download` - Download do CV em PDF
- `GET /health` - Health check da aplicação

## Desenvolvimento Local

### Pré-requisitos

- Python 3.9+
- pip

### Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd MoisesCardosoCV2025
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute a aplicação:
```bash
python -m uvicorn api.index:app --reload
```

4. Acesse no navegador:
```
http://localhost:8000
```

## Deploy na Vercel

### Via CLI

1. Instale a CLI da Vercel:
```bash
npm i -g vercel
```

2. Execute o deploy:
```bash
vercel
```

### Via GitHub

1. Faça push do código para um repositório GitHub
2. Importe o projeto na Vercel Dashboard
3. Configure o projeto (a Vercel detectará automaticamente o vercel.json)
4. Deploy automático a cada push na branch principal

## Testando a API

Exemplos de requisições usando curl:

```bash
# Obter perfil completo
curl https://seu-dominio.vercel.app/api/profile

# Obter experiências
curl https://seu-dominio.vercel.app/api/experience

# Obter skills
curl https://seu-dominio.vercel.app/api/skills

# Obter contato
curl https://seu-dominio.vercel.app/api/contact

# Health check
curl https://seu-dominio.vercel.app/health
```

## Funcionalidades

- Interface web moderna e responsiva
- Design inspirado no LinkedIn
- Download de CV em PDF
- API REST completa com documentação automática (FastAPI Swagger UI em `/docs`)
- CORS habilitado para integração com outros sistemas
- Otimizado para SEO
- Compatível com impressão
- Mobile-friendly

## Documentação da API

Acesse `/docs` para visualizar a documentação interativa gerada automaticamente pelo FastAPI (Swagger UI).

Acesse `/redoc` para visualizar a documentação alternativa (ReDoc).

## Contato

- **Email**: mcardosodeveloper@outlook.com
- **LinkedIn**: [linkedin.com/in/moises-cardoso](https://www.linkedin.com/in/moises-cardoso)
- **Portfolio**: [moises-cardoso-github-io.vercel.app](https://moises-cardoso-github-io.vercel.app/)

## Licença

Este projeto é pessoal e de uso individual.
