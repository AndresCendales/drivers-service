""" Mapeadores para la capa de infrastructura del dominio de drivers

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from alpesonline.seedwork.dominio.repositorios import Mapeador
from alpesonline.seedwork.infraestructura.utils import unix_time_millis
from alpesonline.modulos.drivers.dominio.entidades import Ruta
from alpesonline.modulos.drivers.dominio.eventos import RutaAsignada, EventoRutaAsignada

from .dto import Asignacion as RutaDTO
from .excepciones import NoExisteImplementacionParaTipoFabricaExcepcion


class MapadeadorEventosRuta(Mapeador):
    # Versiones aceptadas
    versions = ('v1',)

    LATEST_VERSION = versions[0]

    def __init__(self):
        self.router = {
            RutaAsignada: self._entidad_a_ruta_asignada,
            # ReservaAprobada: self._entidad_a_reserva_aprobada,
            # ReservaCancelada: self._entidad_a_reserva_cancelada,
            # ReservaPagada: self._entidad_a_reserva_pagada
        }

    def obtener_tipo(self) -> type:
        return EventoRutaAsignada.__class__

    def es_version_valida(self, version):
        for v in self.versions:
            if v == version:
                return True
        return False

    def _entidad_a_ruta_asignada(self, entidad: RutaAsignada, version=LATEST_VERSION):
        def v1(evento):
            from .schema.v1.eventos import RutaAsignadaPayload, EventoRutaAsignada

            payload = RutaAsignadaPayload(
                ruta_id=str(evento.ruta_id),
                driver_id=str(evento.driver_id),
                estado=str(evento.estado),
                fecha_creacion=int(unix_time_millis(evento.fecha_evento))
            )
            evento_integracion = EventoRutaAsignada(id=str(evento.id))
            evento_integracion.id = str(evento.id)
            evento_integracion.time = int(unix_time_millis(evento.fecha_evento))
            evento_integracion.specversion = str(version)
            evento_integracion.type = 'RutaAsignada'
            evento_integracion.datacontenttype = 'AVRO'
            evento_integracion.service_name = 'drivers'
            evento_integracion.data = payload

            return evento_integracion

        if not self.es_version_valida(version):
            raise Exception(f'No se sabe procesar la version {version}')

        if version == 'v1':
            return v1(entidad)

    # def _entidad_a_reserva_aprobada(self, entidad: ReservaAprobada, version=LATEST_VERSION):
    #     # TODO
    #     raise NotImplementedError
    #
    # def _entidad_a_reserva_cancelada(self, entidad: ReservaCancelada, version=LATEST_VERSION):
    #     # TODO
    #     raise NotImplementedError
    #
    # def _entidad_a_reserva_pagada(self, entidad: ReservaPagada, version=LATEST_VERSION):
    #     # TODO
    #     raise NotImplementedError

    def entidad_a_dto(self, entidad: EventoRutaAsignada, version=LATEST_VERSION) -> RutaDTO:
        if not entidad:
            raise NoExisteImplementacionParaTipoFabricaExcepcion
        func = self.router.get(entidad.__class__, None)

        if not func:
            raise NoExisteImplementacionParaTipoFabricaExcepcion

        return func(entidad, version=version)

    def dto_a_entidad(self, dto: RutaDTO, version=LATEST_VERSION) -> Ruta:
        raise NotImplementedError


class MapeadorRuta(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Ruta.__class__

    def entidad_a_dto(self, entidad: Ruta) -> RutaDTO:

        ruta_dto = RutaDTO()
        ruta_dto.fecha_creacion = entidad.fecha_creacion
        ruta_dto.fecha_actualizacion = entidad.fecha_actualizacion
        ruta_dto.zona = entidad.zona
        ruta_dto.hora_salida = entidad.hora_salida
        ruta_dto.tiempo_estimado = entidad.tiempo_estimado
        ruta_dto.driver_id = entidad.id_driver
        return ruta_dto

    def dto_a_entidad(self, dto: RutaDTO) -> Ruta:
        ruta = Ruta(dto.id, dto.fecha_creacion, dto.fecha_actualizacion)
        ruta.zona = dto.zona
        ruta.hora_salida = dto.hora_salida
        ruta.tiempo_estimado = dto.tiempo_estimado
        ruta.id_driver = dto.driver_id
        return ruta