# prue-backend-are
Prueba técnica  gestor de desarrollo web inmobiliaria

# Prueba Técnica – Gestor de Desarrollo Web Inmobiliaria 🏡

Este proyecto implementa el **backend** de una aplicación para inmobiliarias.  
Permite listar y filtrar inmuebles de manera flexible (por ciudad, barrio, tipo, rango de precio y otros atributos).  

Cumple con lo solicitado en la prueba técnica:  
- Landing + buscador dinámico (parte frontend, por implementar).  
- Backend con API RESTful y filtros.  
- Código modular, limpio y documentado.  

---

## 🚀 Tecnologías utilizadas
- [FastAPI](https://fastapi.tiangolo.com/) – Framework web para APIs.
- [Uvicorn](https://www.uvicorn.org/) – Servidor ASGI.
- [Pydantic](https://docs.pydantic.dev/) – Validación de datos.

---

## 📂 Estructura del proyecto

```text
backend/
└─ app/
   ├─ main.py                 # Punto de entrada de FastAPI
   ├─ core/
   │  └─ config.py            # Configuración (CORS, etc.)
   └─ modulo/
      └─ inmuebles/
         ├─ __init__.py
         ├─ models/
         │  ├─ __init__.py
         │  └─ inmuebles_models.py   # Esquemas Pydantic
         ├─ repositories/
         │  ├─ base.py               # Contrato de repositorio
         │  └─ memory_repo.py        # Datos en memoria (semilla)
         ├─ services/
         │  └─ inmuebles_service.py  # Lógica de negocio
         └─ routes/
            └─ inmuebles_routes.py   # Endpoints REST


git clone https://github.com/tu_usuario/prueba-inmobiliaria.git
cd prueba-inmobiliaria/backend


python -m venv venv

# Windows
 venv\Scripts\activate

# Linux / Mac
source  venv/bin/activate


uvicorn app.main:app --reload --port 8000


http://localhost:8000/docs
 (Swagger UI)

