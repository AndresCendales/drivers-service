from pulsar.schema import *
from dataclasses import dataclass, field
from seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoAsignarDriverPayload(ComandoIntegracion):
    id_usuario = String()
    # TODO Cree los records para itinerarios

class ComandoAsignarDriver(ComandoIntegracion):
    data = ComandoAsignarDriverPayload()