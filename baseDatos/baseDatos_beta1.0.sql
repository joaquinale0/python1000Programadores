create database if not exists cinemarkss;

use cinemarkss;

create table if not exists usuario(
	idUsuario int not null auto_increment,
    usuario varchar(50) not null unique,
    contrasena varchar(50) not null,
    administracion int not null default 0,
    tarjeta int default 0,
    fechaNacimiento datetime,
    primary key (idUsuario)
);

create table if not exists sala(
	idSala int not null auto_increment,
    nombreSala varchar(50) default "sin nombre",
    cantidadAsientos int default 0,
    primary key (idSala)
);

select * from horario;

create table if not exists pelicula(
	idPelicula int not null auto_increment,
    titulo varchar (50) default "sin titulo",
    genero varchar (50) default "sin genero",
    duracion datetime,
    categoria int default 0,
    formato int default 0,
    primary key (idPelicula)
);

create table if not exists horario(
	idHorario int not null auto_increment,
    entrada datetime,
    salida datetime,
    horario_idSala int,
    horario_idPelicula int,
	primary key (idHorario),
    foreign key (horario_idSala) references sala(idSala),
    foreign key (horario_idPelicula) references pelicula(idPelicula)
);

create table if not exists asientos(
	idAsientos int not null auto_increment,
    asientoOcupado int,
    asientos_idSala int,
    asientos_idHorario int,
	primary key (idAsientos),
    foreign key (asientos_idSala) references sala(idSala),
    foreign key (asientos_idHorario) references horario(idHorario)
);

create table if not exists reserva(
	idReserva int not null auto_increment,
    butaca int,
    pelicula varchar(45) not null default("sin nombre"),
    reserva_idUsuario int,
    reserva_idSala int,
    reserva_idPelicula int,
    reserva_idHorario int,
    primary key (idReserva),
    foreign key (reserva_idUsuario) references usuario(idUsuario),
	foreign key (reserva_idSala) references sala(idSala),
	foreign key (reserva_idPelicula) references pelicula(idPelicula),
    foreign key (reserva_idHorario) references horario(idHorario)
);

create table if not exists todasReservas(
	idTodasReservas int not null auto_increment,
    todasReservas_idReserva int,
    todasReservas_idUsuario int,
    primary key (idTodasReservas),
    foreign key (todasReservas_idReserva) references reserva(idReserva),
	foreign key (todasReservas_idUsuario) references usuario(idUsuario)
);

select * from todasReservas;


create table if not exists descuento(
	idDescuentos int not null auto_increment,
    dia datetime,
    porcentaje float,
    primary key (idDescuentos)
);