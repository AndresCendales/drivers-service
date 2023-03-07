""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de drivers

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de drivers

"""

from alpesonline.config.db import db
from alpesonline.modulos.drivers.dominio.repositorios import RepositorioRutas, RepositorioEventosRutas
from alpesonline.modulos.drivers.dominio.entidades import Ruta
from alpesonline.modulos.drivers.dominio.fabricas import FabricaRutas
from .dto import Asignacion as AsignacionDTO
from .dto import EventosAsignacion
from .mapeadores import MapeadorRuta, MapadeadorEventosRuta
from uuid import UUID
from pulsar.schema import *


class RepositorioRutasSQLAlchemy(RepositorioRutas):

    def __init__(self):
        self._fabrica_vuelos: FabricaRutas = FabricaRutas()

    @property
    def fabrica_vuelos(self):
        return self._fabrica_vuelos

    def obtener_por_id(self, id: UUID) -> Ruta:
        reserva_dto = db.session.query(AsignacionDTO).filter_by(id=str(id)).one()
        return self.fabrica_vuelos.crear_objeto(reserva_dto, MapeadorRuta())

    def obtener_todos(self) -> list[Ruta]:
        # TODO
        raise NotImplementedError

    def agregar(self, reserva: Ruta):
        reserva_dto = self.fabrica_vuelos.crear_objeto(reserva, MapeadorRuta())

        db.session.add(reserva_dto)

    def actualizar(self, reserva: Ruta):
        # TODO
        raise NotImplementedError

    def eliminar(self, reserva_id: UUID):
        # TODO
        raise NotImplementedError


class RepositorioEventosRutasSQLAlchemy(RepositorioEventosRutas):

    def __init__(self):
        self._fabrica_rutas: FabricaRutas = FabricaRutas()

    @property
    def fabrica_vuelos(self):
        return self._fabrica_rutas

    def obtener_por_id(self, id: UUID) -> Ruta:
        # reserva_dto = db.session.query(ReservaDTO).filter_by(id=str(id)).one()
        # return self.fabrica_vuelos.crear_objeto(reserva_dto, MapadeadorEventosReserva())
        raise NotImplementedError

    def obtener_todos(self) -> list[Ruta]:
        raise NotImplementedError

    def agregar(self, evento):
        asignacion_evento = self.fabrica_vuelos.crear_objeto(evento, MapadeadorEventosRuta())

        parser_payload = JsonSchema(asignacion_evento.data.__class__)
        json_str = parser_payload.encode(asignacion_evento.data)
        print(json_str)
        evento_dto = EventosAsignacion()
        evento_dto.id = str(evento.id)
        evento_dto.id_entidad = str(evento.id)
        evento_dto.fecha_evento = evento.fecha_evento
        evento_dto.version = str(asignacion_evento.specversion)
        evento_dto.tipo_evento = evento.__class__.__name__
        evento_dto.formato_contenido = 'JSON'
        evento_dto.nombre_servicio = str(asignacion_evento.service_name)
        evento_dto.contenido = json_str

        db.session.add(evento_dto)

    def actualizar(self, reserva: Ruta):
        raise NotImplementedError

    def eliminar(self, reserva_id: UUID):
        raise NotImplementedError
