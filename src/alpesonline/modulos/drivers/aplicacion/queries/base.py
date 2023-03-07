from alpesonline.seedwork.aplicacion.queries import QueryHandler
from alpesonline.modulos.drivers.infraestructura.fabricas import FabricaVista
from alpesonline.modulos.drivers.dominio.fabricas import FabricaRutas

class ReservaQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_vista: FabricaVista = FabricaVista()
        self._fabrica_vuelos: FabricaRutas = FabricaRutas()

    @property
    def fabrica_vista(self):
        return self._fabrica_vista
    
    @property
    def fabrica_vuelos(self):
        return self._fabrica_vuelos    