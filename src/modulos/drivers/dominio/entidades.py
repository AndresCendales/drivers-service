"""Entidades del dominio de drivers

En este archivo usted encontrará las entidades del dominio de drivers

"""

from __future__ import annotations
from dataclasses import dataclass, field
import datetime, uuid

import modulos.drivers.dominio.objetos_valor as ov
from modulos.drivers.dominio.eventos import RutaAsignada
from seedwork.dominio.entidades import AgregacionRaiz, Entidad


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
    hora_salida: datetime.datetime = field(default_factory=None)
    tiempo_estimado: int = field(default=0)

    def asignar_ruta(self, ruta: Ruta):
        self.id = uuid.uuid4()
        self.id_driver = ruta.id_driver
        self.estado = ov.EstadoRuta.ASIGNADA
        self.ordenes = ruta.ordenes
        self.zona = ruta.zona
        self.hora_salida = ruta.hora_salida
        self.tiempo_estimado = ruta.tiempo_estimado
        self.fecha_actualizacion = datetime.datetime.now()

        self.agregar_evento(RutaAsignada(
            id=self.id,
            ruta_id=uuid.uuid4(),
            driver_id=self.id_driver,
            estado=self.estado,
            fecha_evento=self.fecha_actualizacion
        ))
        # TODO Agregar evento de compensación

    # def aprobar_reserva(self):
    #     self.estado = ov.EstadoReserva.APROBADA
    #     self.fecha_actualizacion = datetime.datetime.now()
    #
    #     self.agregar_evento(ReservaAprobada(self.id, self.fecha_actualizacion))
    #     # TODO Agregar evento de compensación
    #
    # def cancelar_reserva(self):
    #     self.estado = ov.EstadoReserva.CANCELADA
    #     self.fecha_actualizacion = datetime.datetime.now()
    #
    #     self.agregar_evento(ReservaCancelada(self.id, self.fecha_actualizacion))
    #     # TODO Agregar evento de compensación
    #
    # def pagar_reserva(self):
    #     self.estado = ov.EstadoReserva.PAGADA
    #     self.fecha_actualizacion = datetime.datetime.now()
    #
    #     self.agregar_evento(ReservaPagada(self.id, self.fecha_actualizacion))
    #     # TODO Agregar evento de compensación
