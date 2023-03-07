CREATE TABLE asignaciones(
    id varchar(36) NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Llave primaria',
    fecha_creacion DATETIME NOT NULL COMMENT 'Fecha de creación del registro',
    fecha_actualizacion DATETIME NOT NULL COMMENT 'Fecha de actualización del registro',
    zona VARCHAR(255),
    hora_salida DATETIME NOT NULL COMMENT 'Hora de salida del usuario',
    driver_id VARCHAR(36),
);

CREATE TABLE drivers (
    id varchar(36) NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Llave primaria',
    nombre VARCHAR(255),
)