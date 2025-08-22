# backend/app/modulo/inmuebles/routes/inmuebles_routes.py
from fastapi import APIRouter, Query, Depends, HTTPException
from typing import List, Optional
from app.modulo.inmuebles.models.inmuebles_models import Inmueble, Filtros, Paginacion
from app.modulo.inmuebles.repositories.memory_repo import InmueblesRepoMem
from app.modulo.inmuebles.services.inmuebles_service import InmueblesService

router = APIRouter(prefix="/api/inmuebles", tags=["Inmuebles"])

def get_service():
    # Si luego cambias a SQLiteRepo, solo cambias aquí
    return InmueblesService(InmueblesRepoMem())

# ---------- Colección ----------
@router.get("", response_model=List[Inmueble])
def listar_inmuebles(
    ciudad: Optional[str] = None,
    barrio: Optional[str] = None,
    tipo: Optional[str] = None,
    precio_min: Optional[int] = Query(None, ge=0),
    precio_max: Optional[int] = Query(None, ge=0),
    estado: Optional[str] = Query(None, regex="^(arriendo|venta)$"),
    nuevo: Optional[bool] = None,
    destacado: Optional[bool] = None,
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=100),
    svc: InmueblesService = Depends(get_service),
):
    filtros = Filtros(
        ciudad=ciudad, barrio=barrio, tipo=tipo,
        precio_min=precio_min, precio_max=precio_max,
        estado=estado, nuevo=nuevo, destacado=destacado
    )
    pag = Paginacion(page=page, per_page=per_page)
    return svc.listar(filtros, pag)

@router.get("/ciudades", response_model=List[str])
def ciudades(svc: InmueblesService = Depends(get_service)):
    return svc.ciudades()

@router.get("/barrios", response_model=List[str])
def barrios(ciudad: Optional[str] = None, svc: InmueblesService = Depends(get_service)):
    return svc.barrios(ciudad)

@router.get("/tipos", response_model=List[str])
def tipos(svc: InmueblesService = Depends(get_service)):
    return svc.tipos()

# ---------- Recurso individual ----------
@router.get("/{id}", response_model=Inmueble)
def obtener_inmueble(id: int, svc: InmueblesService = Depends(get_service)):
    inm = svc.obtener(id)
    if not inm:
        raise HTTPException(status_code=404, detail="Inmueble no encontrado")
    return inm
