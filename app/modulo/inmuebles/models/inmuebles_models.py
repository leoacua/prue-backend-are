from typing import Optional, Literal
from pydantic import BaseModel, Field

Estado = Literal["arriendo", "venta"]

class Inmueble(BaseModel):
    id: int
    titulo: str
    ciudad: str
    barrio: str
    tipo: str
    precio: int
    estado: Estado
    nuevo: bool = False
    destacado: bool = False
    imagen: Optional[str] = None
    area_m2: Optional[int] = None
    habitaciones: Optional[int] = None
    banos: Optional[int] = None
    descripcion: Optional[str] = None

class InmuebleCreate(BaseModel):
    titulo: str
    ciudad: str
    barrio: str
    tipo: str
    precio: int = Field(ge=0)
    estado: Estado
    nuevo: bool = False
    destacado: bool = False
    imagen: Optional[str] = None
    area_m2: Optional[int] = None
    habitaciones: Optional[int] = None
    banos: Optional[int] = None
    descripcion: Optional[str] = None

class InmuebleUpdate(BaseModel):
    titulo: Optional[str] = None
    ciudad: Optional[str] = None
    barrio: Optional[str] = None
    tipo: Optional[str] = None
    precio: Optional[int] = Field(default=None, ge=0)
    estado: Optional[Estado] = None
    nuevo: Optional[bool] = None
    destacado: Optional[bool] = None
    imagen: Optional[str] = None
    area_m2: Optional[int] = None
    habitaciones: Optional[int] = None
    banos: Optional[int] = None
    descripcion: Optional[str] = None

class Filtros(BaseModel):
    ciudad: Optional[str] = None
    barrio: Optional[str] = None
    tipo: Optional[str] = None
    precio_min: Optional[int] = Field(default=None, ge=0)
    precio_max: Optional[int] = Field(default=None, ge=0)
    estado: Optional[Estado] = None
    nuevo: Optional[bool] = None
    destacado: Optional[bool] = None

class Paginacion(BaseModel):
    page: int = Field(default=1, ge=1)
    per_page: int = Field(default=10, ge=1, le=100)
