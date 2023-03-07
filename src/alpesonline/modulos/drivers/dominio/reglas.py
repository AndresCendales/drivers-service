"""Reglas de negocio del dominio de cliente

En este archivo usted encontrará reglas de negocio del dominio de cliente

"""

from alpesonline.seedwork.dominio.reglas import ReglaNegocio
from .objetos_valor import Ruta
from datetime import datetime


class HoraSalida(ReglaNegocio):
    ruta: Ruta

    def __init__(self, ruta,
                 mensaje='La ruta propuesta no puede asignarse porque su hora de salida es menor a la hora actual'):
        super().__init__(mensaje)
        self.ruta = ruta

    def es_valido(self) -> bool:
        return self.ruta.hora_salida > datetime.now()
