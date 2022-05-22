use [master]
GO

CREATE DATABASE [BDSGA]
GO

USE BDSGA
GO

CREATE TABLE Articulos (
	IdArticulo INT PRIMARY KEY IDENTITY (1,1) NOT NULL,
	NombreArticulo VARCHAR(40) NOT NULL,
	PrecioVenta int NOT NULL,
	PrecioUnitario int NOT NULL,
	Cantidad int NOT NULL,
	NombreCategoria VARCHAR(40) NOT NULL,
	IdProeevedor int NOT NULL,
);
GO

/*Num Fact, Id Cliente, Empleado, Fecha, Forma Pago, Total, IVA*/

CREATE TABLE Facturacion (
	NumeroFactura VARCHAR(40) PRIMARY KEY  NOT NULL,
	IdCliente INT NOT NULL,
	Empleado VARCHAR(40) NOT NULL,
	Fecha DATE NOT NULL,
	FormaPago VARCHAR(40) NOT NULL,
	Total INT NOT NULL,
	Iva INT NOT NULL
);
GO


CREATE TABLE DetalleFactura (
	IdDetalleFac INT PRIMARY KEY IDENTITY (1,1) NOT NULL,
	NumeroFactura VARCHAR(40) NOT NULL,
	Descripcion VARCHAR(40) NOT NULL,
	Cantidad INT NOT NULL,
	TotalDetalle INT NOT NULL
);
GO

CREATE TABLE Clientes (
	IdCliente INT PRIMARY KEY IDENTITY (1,1) NOT NULL,
	TipoDoc VARCHAR(40) NOT NULL,
	NumeroDocumento INT NOT NULL,
	Nombres VARCHAR(40) NOT NULL,
	Apellidos VARCHAR(40) NOT NULL,
	Direccion VARCHAR(40) NOT NULL,
	Telefono BIGINT NOT NULL,
	Ciudad VARCHAR (40) NOT NULL
);
GO

CREATE TABLE Proeevedores (
	IdProeevedor INT PRIMARY KEY IDENTITY (1,1) NOT NULL,
	TipoDoc VARCHAR(40) NOT NULL,
	NumeroDocumento INT NOT NULL,
	Nombres VARCHAR(40) NOT NULL,
	Apellidos VARCHAR(40) NOT NULL,
	NombreComercial VARCHAR(100) NOT NULL,
	Direccion VARCHAR(40) NOT NULL,
	Ciudad VARCHAR (40) NOT NULL,
	Telefono BIGINT NOT NULL
);
GO

CREATE TABLE Devoluciones (
	IdDevolucion INT PRIMARY KEY IDENTITY (1,1) NOT NULL,
	NumeroFactura VARCHAR(40) NOT NULL,
	IdArticulo INT NOT NULL,
	Cantidad INT NOT NULL,
	Motivo VARCHAR(40) NOT NULL,
	Fecha DATE NOT NULL
);
GO



/*Creacion de la llave foranea para la tabla de articulos*/
ALTER TABLE Articulos
ADD CONSTRAINT FK_Proeevedor
FOREIGN KEY (IdProeevedor) 
REFERENCES Proeevedores (IdProeevedor)
GO
/*Creacion de la llave foranea para la tabla de facturaci n*/
ALTER TABLE Facturacion
ADD CONSTRAINT FK_Cliente
FOREIGN KEY (IdCliente) 
REFERENCES Clientes (IdCliente)
GO

/*Creacion de las llaves foraneas para la tabla de detalle factura*/
ALTER TABLE DetalleFactura
ADD CONSTRAINT FK_Factura
FOREIGN KEY (NumeroFactura) 
REFERENCES Facturacion (NumeroFactura)
GO

/*Devoluciones*/
ALTER TABLE Devoluciones
ADD CONSTRAINT FK_DevolucionNFACT
FOREIGN KEY (NumeroFactura) 
REFERENCES Facturacion (NumeroFactura)
GO

ALTER TABLE Devoluciones
ADD CONSTRAINT FK_DevolucionArticulo
FOREIGN KEY (IdArticulo) 
REFERENCES Articulos (IdArticulo)
GO

CREATE PROCEDURE SP_RegistrarClientes(	
	@TipoDoc as varchar(40),
	@NumeroDoc as BigInt,	
	@Nombres as varchar(40),
	@Apellidos as varchar(40),
	@Direccion as varchar(40),
	@Telefono as BigInt,
	@Ciudad as varchar(40)
	
)
AS 
BEGIN
	INSERT INTO Clientes (TipoDoc, NumeroDocumento, Nombres, Apellidos, Direccion, Telefono, Ciudad)
	VALUES (@TipoDoc, @NumeroDoc, @Nombres,@Apellidos,@Direccion, @Telefono, @Ciudad);
END
GO
/*EXECUTE SP_ActualizarClientes 1,1018208734,'Sebastian', 'Uzuga Quintero', 'Carrera 124', 3124356743
EXECUTE SP_ActualizarClientes 1,1018208735,'Sara Estefania', 'Ruiz Florez', 'Diagonal 123', 3156656743

select * from Clientes
select * from Proeevedores
*/

CREATE PROCEDURE SP_RegistrarProeevedores
(
	@TipoDoc as varchar(40),
	@NumeroDoc as BigInt,	
	@Nombres as varchar(40),
	@Apellidos as varchar(40),
	@NombreComercial as varchar(100),
	@Direccion as varchar(40),
	@Ciudad as varchar(40),
	@Telefono as BigInt
)
AS 
BEGIN
	INSERT INTO Proeevedores (TipoDoc, NumeroDocumento, Nombres, Apellidos, NombreComercial, Direccion, Ciudad, Telefono)
	VALUES (@tipoDoc , @NumeroDoc, @Nombres,@Apellidos,@NombreComercial,@Direccion,@Ciudad,@Telefono);
END
GO
/*
EXECUTE SP_ActualizarProeevedores 1543789432,2,'David', 'Mu oz Gomez', 5

select * from Proeevedores

select * from EmpresasProeevedoras

select * from Clientes
*/


CREATE PROCEDURE SP_RegistarArticulos
(
	@NombreArticulo as varchar(40),
	@PrecioVenta as int,
	@PrecioUnitario as int,
	@Cantidad as varchar(40),
	@NombreCategoria as varchar(40),
	@IdProeevedor as int
)
AS 
BEGIN
	INSERT INTO Articulos(NombreArticulo, PrecioVenta, PrecioUnitario, Cantidad, NombreCategoria, IdProeevedor)
	VALUES (@NombreArticulo, @PrecioVenta, @PrecioUnitario,@Cantidad,@NombreCategoria,@IdProeevedor);
END
GO
/*
EXECUTE SP_RegistarArticulos 'Salchicha de cerdo', 5500, 3000, 100, 1, 1

Select * from Categorias
Select * from Proeevedores

Select * from Articulos
*/

CREATE PROCEDURE SP_ActualizarStock
(
	@ID_Articulo as int,
	@Cantidad as varchar(40)
)
AS 
BEGIN
	UPDATE Articulos
	SET Cantidad=@Cantidad
	WHERE IdArticulo=@ID_Articulo
END
GO
/*
EXECUTE SP_ActualizarStock 1,110
*/


CREATE LOGIN AdminBDSGA WITH PASSWORD = '1234' /* centralizacionCXP en Hexadecimal  */

CREATE USER AdminBDSGA FOR LOGIN AdminBDSGA

ALTER ROLE db_owner ADD member AdminBDSGA
GO


CREATE PROCEDURE SP_RegistrarDetalleFactura(	
	@NumFactura as varchar(40),
	@Descripcion as varchar(40),
	@Cantidad as int,
	@TotalDetalle as int
)
AS 
BEGIN
	INSERT INTO DetalleFactura(NumeroFactura, Descripcion, Cantidad, TotalDetalle)
	VALUES (@NumFactura, @Descripcion, @Cantidad,@TotalDetalle);
END
GO



CREATE PROCEDURE SP_RegistrarFactura(
	@NumFactura as varchar(40),
	@IdCliente as int,	
	@Empleado as varchar(40),
	@Fecha as date,
	@FormaPago as varchar(40),
	@Total as int,
	@Iva as int
)
AS 
BEGIN
	INSERT INTO Facturacion(NumeroFactura, IdCliente, Empleado, Fecha, FormaPago, Total, Iva)
	VALUES (@NumFactura, @IdCliente, @Empleado,@Fecha,@FormaPago, @Total, @Iva);
END
GO

CREATE PROCEDURE SP_RegistrarDevoluciones(	
	@NumFactura as varchar(40),
	@IdArticulo as int,	
	@Cantidad as int,
	@Motivo as varchar(40),
	@Fecha as date
)
AS 
BEGIN
	INSERT INTO Devoluciones(NumeroFactura, IdArticulo, Cantidad, Motivo, Fecha)
	VALUES (@NumFactura, @IdArticulo, @Cantidad,@Motivo,@Fecha);
END
GO