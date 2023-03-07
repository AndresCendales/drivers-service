from alpesonline.seedwork.infraestructura.proyecciones import Proyeccion, ProyeccionHandler
from alpesonline.seedwork.infraestructura.proyecciones import ejecutar_proyeccion as proyeccion
from alpesonline.modulos.drivers.infraestructura.fabricas import FabricaRepositorio
from alpesonline.modulos.drivers.infraestructura.repositorios import RepositorioRutas
from alpesonline.modulos.drivers.dominio.entidades import Ruta
from alpesonline.seedwork.infraestructura.utils import millis_a_datetime
import logging
import traceback
from datetime import datetime
from abc import ABC, abstractmethod


class ProyeccionAsignacion(Proyeccion, ABC):
    @abstractmethod
    def ejecutar(self):
        ...


class ProyeccionAsignacionesLista(ProyeccionAsignacion):
    def __init__(self, id_ruta, id_driver, estado, fecha_creacion, fecha_actualizacion):
        self.id_ruta = id_ruta
        self.id_driver = id_driver
        self.estado = estado
        self.fecha_creacion = millis_a_datetime(fecha_creacion)
        self.fecha_actualizacion = millis_a_datetime(fecha_actualizacion)

    def ejecutar(self, db=None):
        if not db:
            logging.error('ERROR: DB del app no puede ser nula')
            return

        fabrica_repositorio = FabricaRepositorio()
        repositorio = fabrica_repositorio.crear_objeto(RepositorioRutas)
        print(f"ejecutnado proyeccion")
        
        print(self.id_ruta)
        print(self.id_driver)
        print(self.estado)
        print(self.fecha_creacion)
        print(self.fecha_actualizacion)
        repositorio.agregar(
            Ruta(
                id = self.id_ruta,
                id_driver=self.id_driver,
                estado=self.estado,
                hora_salida=datetime.now(),
            )
        )

        db.session.commit()


class ProyeccionReservaHandler(ProyeccionHandler):

    def handle(self, proyeccion: ProyeccionAsignacion):
        # TODO El evento de creación no viene con todos los datos de itinerarios, esto tal vez pueda ser una extensión
        # Asi mismo estamos dejando la funcionalidad de persistencia en el mismo método de recepción. Piense que componente
        # podriamos diseñar para alojar esta funcionalidad
        from alpesonline.config.db import db

        proyeccion.ejecutar(db=db)


@proyeccion.register(ProyeccionAsignacionesLista)
def ejecutar_proyeccion_reserva(proyeccion, app=None):
    if not app:
        logging.error('ERROR: Contexto del app no puede ser nulo')
        return
    try:
        with app.app_context():
            handler = ProyeccionReservaHandler()
            handler.handle(proyeccion)

    except Exception as e:
        traceback.print_exc()
        logging.error('ERROR: Persistiendo!')
        logging.error(e)