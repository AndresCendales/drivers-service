from modulos.drivers.dominio.eventos import RutaAsignada
from seedwork.aplicacion.handlers import Handler
from modulos.drivers.infraestructura.despachadores import Despachador

class HandlerReservaIntegracion(Handler):

    @staticmethod
    def handle_ruta_asignada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-rutas')


    