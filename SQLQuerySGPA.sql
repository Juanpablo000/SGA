CREATE TABLE Articulos (
	IdArticulo INT PRIMARY KEY IDENTITY (1,1) NOT NULL,
	NombreArticulo VARCHAR(40) NOT NULL,
	PrecioVenta int NOT NULL,
	PrecioUnitario int NOT NULL,
	Cantidad int NOT NULL,
	IdCategoria int NOT NULL,
	IdProeevedor int NOT NULL,
);

CREATE TABLE Facturacion (
	IdFactura INT PRIMARY KEY IDENTITY (1,1) NOT NULL,
	IdPago INT NOT NULL,
	Fecha DATE NOT NULL,
	IdCliente INT NOT NULL,
);

CREATE TABLE Categorias (
	IdCategoria INT PRIMARY KEY IDENTITY (1,1) NOT NULL,
	NombreCategoria VARCHAR(40) NOT NULL,
);

CREATE TABLE FormasPago (
	IdPago INT PRIMARY KEY IDENTITY (1,1) NOT NULL,
	NombrePago VARCHAR(40) NOT NULL,
);

CREATE TABLE DetalleFactura (
	IdDetalleFac INT PRIMARY KEY IDENTITY (1,1) NOT NULL,
	IdFactura INT NOT NULL,
	Cantidad INT NOT NULL,
	IdProducto INT NOT NULL,
);

CREATE TABLE Clientes (
	IdCliente INT PRIMARY KEY IDENTITY (1,1) NOT NULL,
	IdTipoDocumento INT NOT NULL,
	NumeroDocumento INT NOT NULL,
	Nombres VARCHAR(40) NOT NULL,
	Apellidos VARCHAR(40) NOT NULL,
	Direccion VARCHAR(40) NOT NULL,
	Telefono BIGINT NOT NULL,
);

CREATE TABLE Proeevedores (
	IdProeevedor INT PRIMARY KEY IDENTITY (1,1) NOT NULL,
	IdTipoDocumento INT NOT NULL,
	NumeroDocumento INT NOT NULL,
	Nombres VARCHAR(40) NOT NULL,
	Apellidos VARCHAR(40) NOT NULL,
	IdEmpresa INT NOT NULL,
);

CREATE TABLE EmpresasProeevedoras (
	IdEmpresa INT PRIMARY KEY IDENTITY (1,1) NOT NULL,
	Nombre VARCHAR(100) NOT NULL,
	Direccion VARCHAR(40) NOT NULL,
	Ciudad VARCHAR(40) NOT NULL,
	Telefono BIGINT NOT NULL,
);

drop table TipoDocumento

CREATE TABLE TipoDocumento (
	IdTipoDocumento INT PRIMARY KEY IDENTITY (1,1) NOT NULL,
	NomDocumento VARCHAR(40) NOT NULL,
);


/*Creacion de la llave foranea para la tabla de articulos*/
ALTER TABLE Articulos
ADD CONSTRAINT FK_Categoria
FOREIGN KEY (IdCategoria) 
REFERENCES Categorias (IdCategoria)

ALTER TABLE Articulos
ADD CONSTRAINT FK_Proeevedor
FOREIGN KEY (IdProeevedor) 
REFERENCES Proeevedores (IdProeevedor)

/*Creacion de la llave foranea para la tabla de facturaci�n*/
ALTER TABLE Facturacion
ADD CONSTRAINT FK_Pago
FOREIGN KEY (IdPago) 
REFERENCES FormasPago (IdPago)


ALTER TABLE Facturacion
ADD CONSTRAINT FK_Cliente
FOREIGN KEY (IdCliente) 
REFERENCES Clientes (IdCliente)


/*Creacion de las llaves foraneas para la tabla de detalle factura*/
ALTER TABLE DetalleFactura
ADD CONSTRAINT FK_Factura
FOREIGN KEY (IdFactura) 
REFERENCES Facturacion (IdFactura)


ALTER TABLE DetalleFactura
ADD CONSTRAINT FK_Articulo
FOREIGN KEY (IdProducto) 
REFERENCES Articulos (IdArticulo)

/*Creacion de las llaves foraneas para la tabla de proeevedores*/
ALTER TABLE Proeevedores
ADD CONSTRAINT FK_Empresa
FOREIGN KEY (IdEmpresa) 
REFERENCES EmpresasProeevedoras (IdEmpresa)

/*Clientes*/
ALTER TABLE Clientes
ADD CONSTRAINT FK_Documento
FOREIGN KEY (IdTipoDocumento) 
REFERENCES TipoDocumento (IdTipoDocumento)

select * from Clientes

CREATE PROCEDURE SP_ActualizarClientes
(
@IdDoc as int,
@NumeroDoc as BigInt,
@Nombres as varchar(40),
@Apellidos as varchar(40),
@Direccion as varchar(40),
@Telefono as BigInt
)
AS 
BEGIN
	INSERT INTO Clientes (IdTipoDocumento, NumeroDocumento, Nombres, Apellidos, Direccion, Telefono)
	VALUES (@IdDoc, @NumeroDoc, @Nombres,@Apellidos,@Direccion, @Telefono);
END

EXECUTE SP_ActualizarClientes 1,1018208734,'Sebastian', 'Uzuga Quintero', 'Carrera 124', 3124356743
EXECUTE SP_ActualizarClientes 1,1018208735,'Sara Estefania', 'Ruiz Florez', 'Diagonal 123', 3156656743

select * from Clientes
select * from Proeevedores

CREATE PROCEDURE SP_ActualizarProeevedores
(
@NumeroDoc as BigInt,
@IdDoc as int,
@Nombres as varchar(40),
@Apellidos as varchar(40),
@IdEmpresa as int
)
AS 
BEGIN
	INSERT INTO Proeevedores (IdTipoDocumento, NumeroDocumento, Nombres, Apellidos, IdEmpresa)
	VALUES (@IdDoc, @NumeroDoc, @Nombres,@Apellidos,@IdEmpresa);
END

EXECUTE SP_ActualizarProeevedores 1543789432,2,'David', 'Mu�oz Gomez', 5

select * from Proeevedores

select * from EmpresasProeevedoras

select * from Clientes


CREATE PROCEDURE SP_RegistarArticulos
(
@NombreArticulo as varchar(40),
@PrecioVenta as int,
@PrecioUnitario as int,
@Cantidad as varchar(40),
@IdCategoria as varchar(40),
@IdProeevedor as int
)
AS 
BEGIN
	INSERT INTO Articulos(NombreArticulo, PrecioVenta, PrecioUnitario, Cantidad, IdCategoria, IdProeevedor)
	VALUES (@NombreArticulo, @PrecioVenta, @PrecioUnitario,@Cantidad,@IdCategoria,@IdProeevedor);
END

EXECUTE SP_RegistarArticulos 'Salchicha de cerdo', 5500, 3000, 100, 1, 1

Select * from Categorias
Select * from Proeevedores

Select * from Articulos

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

EXECUTE SP_ActualizarStock 1,110


Select * from Articulos