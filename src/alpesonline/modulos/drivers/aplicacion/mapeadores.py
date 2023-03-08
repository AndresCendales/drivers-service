from alpesonline.seedwork.aplicacion.dto import Mapeador as AppMap
from alpesonline.seedwork.dominio.repositorios import Mapeador as RepMap
from alpesonline.modulos.drivers.dominio.entidades import Ruta
from alpesonline.modulos.drivers.dominio.objetos_valor import Orden, Ubicacion, ZonaEnum, TipoOrdenEnum
from .dto import RutaDTO, UbicacionDTO, OrdenDTO
import logging
from datetime import datetime


class MapeadorRutaDTOJson(AppMap):
    def _procesar_ruta(self, ruta: dict) -> RutaDTO:
        ordenes: list[OrdenDTO] = list()
        for orden in ruta.get('ordenes', list()):
            ordenes.append(
                OrdenDTO(
                    id=orden.get('id'),
                    origen=self._procesar_ubicacion(orden.get('origen')),
                    destino=self._procesar_ubicacion(orden.get('destino')),
                    tipo=orden.get('tipo'),
                    parada=orden.get('parada')
                )
            )
        return RutaDTO(
            id=ruta.get('ruta_id'),
            ordenes=ordenes,
            zona=ruta.get('zona'),
            hora_salida=ruta.get('hora_salida'),
            tiempo_estimado=ruta.get('tiempo_estimado')
        )

    @staticmethod
    def _procesar_ubicacion(ubicacion: dict) -> UbicacionDTO:
        return UbicacionDTO(ubicacion.get('lat'), ubicacion.get('lon'))

    def externo_a_dto(self, externo: dict) -> RutaDTO:
        return self._procesar_ruta(externo)

    def dto_a_externo(self, dto: RutaDTO) -> dict:
        return dto.__dict__


class MapeadorRuta(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_ruta(self, ruta_dto: RutaDTO) -> list[Orden]:
        ordenes: list[Orden] = list()
        try:
            for orden in ruta_dto.ordenes:
                ordenes.append(
                    Orden(
                        id=orden.id,
                        origen=Ubicacion(orden.origen.lat, orden.origen.lon),
                        destino=Ubicacion(orden.destino.lat, orden.destino.lon),
                        tipo=TipoOrdenEnum(orden.tipo),
                        parada=orden.parada
                    )
                )
        except Exception as e:
            logging.error(e.__str__())
        return ordenes

    def obtener_tipo(self) -> type:
        return Ruta.__class__

    def entidad_a_dto(self, entidad: Ruta) -> RutaDTO:

        ordenes: list[OrdenDTO] = list()
        for orden in entidad.ordenes:
            ordenes.append(
                OrdenDTO(
                    origen=UbicacionDTO(orden.origen.lat, orden.origen.lon),
                    destino=UbicacionDTO(orden.destino.lat, orden.destino.lon),
                    tipo=orden.tipo.__str__(),
                    parada=orden.parada
                )
            )

        return RutaDTO(
            fecha_creacion=entidad.fecha_creacion.strftime(self._FORMATO_FECHA),
            fecha_actualizacion=entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA),
            ordenes=ordenes,
            zona=entidad.zona.__str__(),
            hora_salida=entidad.hora_salida.strftime(self._FORMATO_FECHA),
            tiempo_estimado=entidad.tiempo_estimado
        )

    def dto_a_entidad(self, dto: RutaDTO) -> Ruta:
        return Ruta(
            fecha_creacion=datetime.now(),
            fecha_actualizacion=datetime.now(),
            ordenes=self._procesar_ruta(dto),
            zona=ZonaEnum(dto.zona),
            hora_salida=datetime.strptime(dto.hora_salida, self._FORMATO_FECHA),
            tiempo_estimado=dto.tiempo_estimado
        )



