create table informes
(
    idinforme integer primary key,--Toca darle un inicio de 2000 en la base de datos
    asunto varchar(150) not null,
    descrip_informe text not null,
    encargado integer not null-- este es el codigo del coordinador
);

-----------------------------------------------------------------------------------------------
-- estas lineas son para aumentar un nuevo atributo en la tabla eventos para que me diga que 
-- si esta 'A' habilidato, 'I' de inhabilitado y  'E' de en espera
-----------------------------------------------------------------------------------------------
alter table eventos add column estado_evento char(1); -- se crea el atributo estado_evento en la tabla eventos
update eventos set estado_evento = 'A';-- se llenan los atributos creados con el valor de habilitado
alter table eventos alter column estado_evento set default 'A';-- Se establece que por defecto el evento esta activo
