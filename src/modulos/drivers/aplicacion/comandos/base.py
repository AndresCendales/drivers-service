from seedwork.aplicacion.comandos import ComandoHandler
from modulos.drivers.infraestructura.fabricas import FabricaRepositorio
from modulos.drivers.dominio.fabricas import FabricaRutas


class AsignarRutaBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_rutas: FabricaRutas = FabricaRutas()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_rutas(self):
        return self._fabrica_rutas
