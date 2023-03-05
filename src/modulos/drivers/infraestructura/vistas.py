from seedwork.infraestructura.vistas import Vista
from modulos.drivers.dominio.entidades import Ruta
from config.db import db
from .dto import Ruta as RutaDTO

class VistaRuta(Vista):
    def obtener_por(id=None, estado=None, id_cliente=None, **kwargs) -> [Ruta]:
        params = dict()

        if id:
            params['id'] = str(id)
        
        if estado:
            params['estado'] = str(estado)
        
        if id_cliente:
            params['id_cliente'] = str(id_cliente)
            
        # TODO Convierta ReservaDTO a Reserva y valide que la consulta es correcta
        return db.session.query(RutaDTO).filter_by(**params)
