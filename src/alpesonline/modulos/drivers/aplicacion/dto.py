from dataclasses import dataclass, field
from alpesonline.seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class UbicacionDTO(DTO):
    lat: float = field(default_factory=float)
    lon: float = field(default_factory=float)


@dataclass(frozen=True)
class OrdenDTO(DTO):
    id: str = field(default_factory=str)
    origen: UbicacionDTO = field(default_factory=UbicacionDTO)
    destino: UbicacionDTO = field(default_factory=UbicacionDTO)
    tipo: str = field(default_factory=str)
    parada: int = field(default_factory=int)


@dataclass(frozen=True)
class RutaDTO(DTO):
    id: str = field(default_factory=str)
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    ordenes: list[OrdenDTO] = field(default_factory=list)
    zona: str = field(default_factory=str)
    hora_salida: str = field(default_factory=str)
    tiempo_estimado: int = field(default_factory=int)
