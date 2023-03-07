from alpesonline.seedwork.aplicacion.queries import Query, QueryResultado
from alpesonline.seedwork.aplicacion.queries import ejecutar_query as query
from alpesonline.modulos.drivers.dominio.entidades import Ruta
from dataclasses import dataclass
from .base import ReservaQueryBaseHandler
from alpesonline.modulos.drivers.aplicacion.mapeadores import MapeadorRuta


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
