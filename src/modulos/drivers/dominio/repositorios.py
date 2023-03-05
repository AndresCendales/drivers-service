""" Interfaces para los repositorios del dominio de drivers

En este archivo usted encontrará las diferentes interfaces para repositorios
del dominio de drivers

"""

from abc import ABC
from seedwork.dominio.repositorios import Repositorio

class RepositorioRutas(Repositorio, ABC):
    ...

class RepositorioEventosRutas(Repositorio, ABC):
    ...
#
# class RepositorioProveedores(Repositorio, ABC):
#     ...