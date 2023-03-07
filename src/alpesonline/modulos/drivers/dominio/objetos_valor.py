"""Objetos valor del dominio de drivers

En este archivo usted encontrará los objetos valor del dominio de drivers

"""

from __future__ import annotations

from dataclasses import dataclass
from alpesonline.seedwork.dominio.objetos_valor import ObjetoValor
from datetime import datetime
from enum import Enum


class ZonaEnum(str, Enum):
    NORTE = 'norte'
    SUR = 'sur'
    ESTE = 'este'
    OESTE = 'oeste'


class EstadoRuta(str, Enum):
    SIN_ASIGNAR = 'sin_asignar'
    ASIGNADA = 'asignada'


class TipoOrdenEnum(str,Enum):
    TARJETA = 'tarjeta'
    RESTAURANTE = 'restaurante'
    MERCADO = 'mercado'


@dataclass(frozen=True)
class Orden(ObjetoValor):
    id: str
    origen: Ubicacion
    destino: Ubicacion
    tipo: TipoOrdenEnum
    parada: int


@dataclass(frozen=True)
class Ubicacion(ObjetoValor):
    lat: float
    lon: float


@dataclass(frozen=True)
class Ruta(ObjetoValor):
    fecha_creacion: datetime
    fecha_actualizacion: datetime
    ordenes: list[Orden]
    zona: ZonaEnum
    hora_salida: datetime
    tiempo_estimado: int

    def primera_parada(self) -> Ubicacion:
        return self.ordenes[0].origen

    def ultima_parada(self) -> Ubicacion:
        return self.ordenes[-1].destino


@dataclass(frozen=True)
class NombreDriver(ObjetoValor):
    nombre: str
