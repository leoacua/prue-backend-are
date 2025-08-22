from typing import List, Optional
from app.modulo.inmuebles.models import Inmueble, Filtros, Paginacion
from app.modulo.inmuebles.repositories.base import InmueblesRepo

DATA: List[Inmueble] = [
    Inmueble(id=1, titulo="Apto moderno en Chapinero", ciudad="Bogotá", barrio="Chapinero",
             tipo="apartamento", precio=220000000, estado="venta", nuevo=True, destacado=True),
    Inmueble(id=2, titulo="Casa familiar en Laureles", ciudad="Medellín", barrio="Laureles",
             tipo="casa", precio=350000000, estado="venta"),
    Inmueble(id=3, titulo="Estudio en El Poblado", ciudad="Medellín", barrio="El Poblado",
             tipo="apartamento", precio=2200000, estado="arriendo", destacado=True),
    Inmueble(id=4, titulo="Casa campestre en Jamundí", ciudad="Cali", barrio="Jamundí",
             tipo="casa", precio=1800000, estado="arriendo", nuevo=True),
]

class InmueblesRepoMem(InmueblesRepo):
    def __init__(self):
        self._data = DATA

    def _aplicar_filtros(self, f: Filtros) -> List[Inmueble]:
        res = self._data
        if f.ciudad:     res = [x for x in res if x.ciudad.lower() == f.ciudad.lower()]
        if f.barrio:     res = [x for x in res if x.barrio.lower() == f.barrio.lower()]
        if f.tipo:       res = [x for x in res if x.tipo.lower() == f.tipo.lower()]
        if f.estado:     res = [x for x in res if x.estado == f.estado]
        if f.precio_min is not None: res = [x for x in res if x.precio >= f.precio_min]
        if f.precio_max is not None: res = [x for x in res if x.precio <= f.precio_max]
        if f.nuevo is not None:      res = [x for x in res if x.nuevo == f.nuevo]
        if f.destacado is not None:  res = [x for x in res if x.destacado == f.destacado]
        return res

    def listar(self, filtros: Filtros, pag: Paginacion) -> List[Inmueble]:
        res = self._aplicar_filtros(filtros)
        start = (pag.page - 1) * pag.per_page
        end = start + pag.per_page
        return res[start:end]

    def obtener(self, id_inmueble: int) -> Optional[Inmueble]:
        return next((x for x in self._data if x.id == id_inmueble), None)

    def ciudades(self) -> List[str]:
        return sorted(list({x.ciudad for x in self._data}))

    def barrios(self, ciudad: Optional[str] = None) -> List[str]:
        if ciudad:
            return sorted(list({x.barrio for x in self._data if x.ciudad.lower() == ciudad.lower()}))
        return sorted(list({x.barrio for x in self._data}))

    def tipos(self) -> List[str]:
        return sorted(list({x.tipo for x in self._data}))
