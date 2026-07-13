create database ClinicaMedica;
go
use ClinicaMedica;
go
create table Registros
(
	Codigo int identity(1,1) primary key,
	Nombre_Servicio varchar(50),
	Costo_Base decimal (8,2),
	Nombre varchar(50),
	Apellido varchar(50),
	Cedula varchar(10),
	Email varchar (50)
)
