from seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from seedwork.aplicacion.queries import ejecutar_query as query
from modulos.drivers.infraestructura.repositorios import RepositorioRutas
from modulos.drivers.dominio.entidades import Ruta
from dataclasses import dataclass
from .base import ReservaQueryBaseHandler
from modulos.drivers.aplicacion.mapeadores import MapeadorRuta
import uuid


@dataclass
class ObtenerReserva(Query):
    id: str


class ObtenerReservaHandler(ReservaQueryBaseHandler):

    def handle(self, query: ObtenerReserva) -> QueryResultado:
        vista = self.fabrica_vista.crear_objeto(Ruta)
        reserva = self.fabrica_vuelos.crear_objeto(vista.obtener_por(id=query.id)[0], MapeadorRuta())
        return QueryResultado(resultado=reserva)


@query.register(ObtenerReserva)
def ejecutar_query_obtener_reserva(query: ObtenerReserva):
    handler = ObtenerReservaHandler()
    return handler.handle(query)
