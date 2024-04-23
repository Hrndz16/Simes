create table informes
(
    idinforme integer primary key,--Toca darle un inicio de 2000 en la base de datos
    asunto varchar(150) not null,
    descrip_informe text not null,
    encargado not null-- este es el codigo del coordinador
)