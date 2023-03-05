from pydispatch import dispatcher

from .handlers import HandlerReservaIntegracion

from modulos.drivers.dominio.eventos import RutaAsignada

dispatcher.connect(HandlerReservaIntegracion.handle_ruta_asignada, signal=f'{RutaAsignada.__name__}Integracion')
