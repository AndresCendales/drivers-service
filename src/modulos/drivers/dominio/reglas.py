"""Reglas de negocio del dominio de cliente

En este archivo usted encontrará reglas de negocio del dominio de cliente

"""

from seedwork.dominio.reglas import ReglaNegocio
from .objetos_valor import Ruta
from datetime import datetime


class RutaValida(ReglaNegocio):
    ruta: Ruta

    def __init__(self, ruta, mensaje='La ruta propuesta es incorrecta'):
        super().__init__(mensaje)
        self.ruta = ruta

    def es_valido(self) -> bool:
        return self.ruta.hora_salida > datetime.now()
