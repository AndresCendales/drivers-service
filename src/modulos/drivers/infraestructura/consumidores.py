import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
import datetime

from modulos.drivers.infraestructura.schema.v1.eventos import EventoRutaAsignada
from modulos.drivers.infraestructura.schema.v1.comandos import ComandoAsignarDriver


from modulos.drivers.infraestructura.proyecciones import ProyeccionReservasLista
from seedwork.infraestructura.proyecciones import ejecutar_proyeccion
from seedwork.infraestructura import utils

def suscribirse_a_eventos(app=None):
    # return
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe(
            'eventos-rutas',
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name='aeroalpes-sub-eventos',
            schema=AvroSchema(EventoRutaAsignada)
        )

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Evento recibido: {datos}')

            # TODO Identificar el tipo de CRUD del evento: Creacion, actualización o eliminación.
            # ejecutar_proyeccion(ProyeccionReservasTotales(datos.fecha_creacion, ProyeccionReservasTotales.ADD), app=app)
            ejecutar_proyeccion(ProyeccionReservasLista(datos.id_reserva, datos.id_cliente, datos.estado, datos.fecha_creacion, datos.fecha_creacion), app=app)
            
            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos(app=None):
    # return
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe(
            topic='comandos-reserva',
            consumer_type=_pulsar.ConsumerType.Shared,
            subscription_name='aeroalpes-sub-comandos',
            schema=AvroSchema(ComandoAsignarDriver))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except Exception as e:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()