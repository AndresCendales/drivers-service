from alpesonline.seedwork.infraestructura.vistas import Vista
from alpesonline.modulos.drivers.dominio.entidades import Ruta
from alpesonline.config.db import db
from .dto import Asignacion as RutaDTO


class VistaRuta(Vista):
    @staticmethod
    def obtener_por(id=None, estado=None, id_cliente=None, **kwargs) -> [Ruta]:
        params = dict()

        if id:
            params['id'] = str(id)

        if estado:
            params['estado'] = str(estado)

        if id_cliente:
            params['id_cliente'] = str(id_cliente)

        return db.session.query(RutaDTO).filter_by(**params)
