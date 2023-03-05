from seedwork.infraestructura.proyecciones import Proyeccion, ProyeccionHandler
from seedwork.infraestructura.proyecciones import ejecutar_proyeccion as proyeccion
from modulos.drivers.infraestructura.fabricas import FabricaRepositorio
from modulos.drivers.infraestructura.repositorios import RepositorioRutas
from modulos.drivers.dominio.entidades import Ruta
# from modulos.drivers.infraestructura.dto import Reserva as ReservaDTO

from seedwork.infraestructura.utils import millis_a_datetime
import datetime
import logging
import traceback
from abc import ABC, abstractmethod
# from .dto import ReservaAnalitica

class ProyeccionReserva(Proyeccion, ABC):
    @abstractmethod
    def ejecutar(self):
        ...


class ProyeccionReservasLista(ProyeccionReserva):
    def __init__(self, id_reserva, id_cliente, estado, fecha_creacion, fecha_actualizacion):
        self.id_reserva = id
        self.id_cliente = id_cliente
        self.estado = estado
        self.fecha_creacion = millis_a_datetime(fecha_creacion)
        self.fecha_actualizacion = millis_a_datetime(fecha_actualizacion)
    
    def ejecutar(self, db=None):
        if not db:
            logging.error('ERROR: DB del app no puede ser nula')
            return
        
        fabrica_repositorio = FabricaRepositorio()
        repositorio = fabrica_repositorio.crear_objeto(RepositorioRutas)
        
        # TODO Haga los cambios necesarios para que se consideren los itinerarios, demás entidades y asociaciones
        repositorio.agregar(
            Ruta(
                id=str(self.id_reserva), 
                id_cliente=str(self.id_cliente), 
                estado=str(self.estado), 
                fecha_creacion=self.fecha_creacion, 
                fecha_actualizacion=self.fecha_actualizacion))
        
        # TODO ¿Y si la reserva ya existe y debemos actualizarla? Complete el método para hacer merge

        # TODO ¿Tal vez podríamos reutilizar la Unidad de Trabajo?
        db.session.commit()

class ProyeccionReservaHandler(ProyeccionHandler):
    
    def handle(self, proyeccion: ProyeccionReserva):

        # TODO El evento de creación no viene con todos los datos de itinerarios, esto tal vez pueda ser una extensión
        # Asi mismo estamos dejando la funcionalidad de persistencia en el mismo método de recepción. Piense que componente
        # podriamos diseñar para alojar esta funcionalidad
        from config.db import db

        proyeccion.ejecutar(db=db)
        

@proyeccion.register(ProyeccionReservasLista)
def ejecutar_proyeccion_reserva(proyeccion, app=None):
    if not app:
        logging.error('ERROR: Contexto del app no puede ser nulo')
        return
    try:
        with app.app_context():
            handler = ProyeccionReservaHandler()
            handler.handle(proyeccion)
            
    except:
        traceback.print_exc()
        logging.error('ERROR: Persistiendo!')
    