""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de drivers

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de drivers

"""

from dataclasses import dataclass
from alpesonline.seedwork.dominio.fabricas import Fabrica
from alpesonline.seedwork.dominio.repositorios import Repositorio
from alpesonline.seedwork.infraestructura.vistas import Vista
from alpesonline.modulos.drivers.infraestructura.vistas import VistaRuta
from alpesonline.modulos.drivers.dominio.entidades import Ruta
from alpesonline.modulos.drivers.dominio.repositorios import RepositorioRutas, RepositorioEventosRutas
from .repositorios import RepositorioRutasSQLAlchemy, \
    RepositorioEventosRutasSQLAlchemy
from .excepciones import ExcepcionFabrica


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioRutas:
            return RepositorioRutasSQLAlchemy()
        elif obj == RepositorioEventosRutas:
            return RepositorioEventosRutasSQLAlchemy()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')


@dataclass
class FabricaVista(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Vista:
        if obj == Ruta:
            return VistaRuta()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')
