from typing import List, Optional
from app.modulo.inmuebles.models import Inmueble, Filtros, Paginacion
from app.modulo.inmuebles.repositories.base import InmueblesRepo

class InmueblesService:
    def __init__(self, repo: InmueblesRepo):
        self.repo = repo

    def listar(self, filtros: Filtros, pag: Paginacion) -> List[Inmueble]:
        return self.repo.listar(filtros, pag)

    def obtener(self, id_inmueble: int) -> Optional[Inmueble]:
        return self.repo.obtener(id_inmueble)

    def ciudades(self) -> List[str]:
        return self.repo.ciudades()

    def barrios(self, ciudad: Optional[str] = None) -> List[str]:
        return self.repo.barrios(ciudad)

    def tipos(self) -> List[str]:
        return self.repo.tipos()

