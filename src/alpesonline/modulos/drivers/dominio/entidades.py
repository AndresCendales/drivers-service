"""Entidades del dominio de drivers

En este archivo usted encontrará las entidades del dominio de drivers

"""

from __future__ import annotations
from dataclasses import dataclass, field
import datetime, uuid

import alpesonline.modulos.drivers.dominio.objetos_valor as ov
from alpesonline.modulos.drivers.dominio.eventos import RutaAsignada
from alpesonline.seedwork.dominio.entidades import AgregacionRaiz, Entidad


@dataclass
class Driver(Entidad):
    nombre: ov.NombreDriver = field(default_factory=ov.NombreDriver)
    zona: ov.Zona = field(default=ov.ZonaEnum.NORTE)


@dataclass
class Ruta(AgregacionRaiz):
    id_driver: uuid.UUID = field(hash=True, default=None)
    estado: ov.EstadoRuta = field(default=ov.EstadoRuta.SIN_ASIGNAR)
    ordenes: list[ov.Orden] = field(default_factory=list[ov.Orden])
    zona: ov.Zona = field(default=ov.ZonaEnum.NORTE)
    hora_salida: datetime.datetime = field(default=datetime.datetime.now())
    tiempo_estimado: int = field(default=0)

    def asignar_ruta(self, ruta: Ruta):
        self.id_driver = uuid.uuid4()  # TODO: Asignar id_driver mas cercano
        self.estado = ov.EstadoRuta.ASIGNADA
        self.fecha_actualizacion = datetime.datetime.now()

        self.agregar_evento(RutaAsignada(
            id=self.id,
            ruta_id=uuid.uuid4(),
            driver_id=self.id_driver,
            estado=self.estado,
            fecha_evento=self.fecha_actualizacion
        ))
        # TODO Agregar evento de compensación

