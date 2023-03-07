""" Fábricas para la creación de objetos del dominio de drivers

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de drivers

"""

from .entidades import Ruta
from .reglas import HoraSalida
from .excepciones import TipoObjetoNoExisteEnDominioDriversExcepcion
from alpesonline.seedwork.dominio.repositorios import Mapeador
from alpesonline.seedwork.dominio.fabricas import Fabrica
from alpesonline.seedwork.dominio.entidades import Entidad
from alpesonline.seedwork.dominio.eventos import EventoDominio
from dataclasses import dataclass


@dataclass
class _FabricaRuta(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad) or isinstance(obj, EventoDominio):
            return mapeador.entidad_a_dto(obj)
        else:
            ruta: Ruta = mapeador.dto_a_entidad(obj)

            self.validar_regla(HoraSalida(ruta))
            return ruta


@dataclass
class FabricaRutas(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Ruta.__class__:
            fabrica_ruta = _FabricaRuta()
            return fabrica_ruta.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioDriversExcepcion()
