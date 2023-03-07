from __future__ import annotations
from dataclasses import dataclass
from alpesonline.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime
import uuid


class EventoRutaAsignada(EventoDominio):
    ...


@dataclass
class RutaAsignada(EventoRutaAsignada):
    ruta_id: uuid.UUID = None
    driver_id: uuid.UUID = None
    estado: str = None
    fecha_asignacion: datetime = None

# @dataclass
# class ReservaCancelada(EventoReserva):
#     id_reserva: uuid.UUID = None
#     fecha_actualizacion: datetime = None
#
# @dataclass
# class ReservaAprobada(EventoReserva):
#     id_reserva: uuid.UUID = None
#     fecha_actualizacion: datetime = None
#
# @dataclass
# class ReservaPagada(EventoReserva):
#     id_reserva: uuid.UUID = None
#     fecha_actualizacion: datetime = None
