
CREATE DATABASE dresscode_db;
USE dresscode_db;
DROP TABLE IF EXISTS `administrador`;

CREATE TABLE `administrador` (
  `idUsuario` int NOT NULL AUTO_INCREMENT,
  `Password` varchar(45) DEFAULT NULL,
  `fecha_registro` date DEFAULT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `direccion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idUsuario`)
) ;




INSERT INTO `administrador` VALUES (1,'perrito','2023-10-11','admi','admiss','mendoza'),(2,'gatito','2023-10-11','admi2','admiss2','jujuy 1234');



--
-- Table structure for table `categoria`
--



CREATE TABLE `categoria` (
  `idCategoria` int NOT NULL,
  `Categoria` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idCategoria`)
) ;







CREATE TABLE `proveedores` (
  `idproveedor` int not null AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `contacto` varchar(100) DEFAULT NULL,
  `direccion` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`idproveedor`)
) ;



CREATE TABLE `productos` (
  `idproducto` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `descripcion` text,
  `precio` decimal(10,2) NOT NULL,
  `stock` int NOT NULL,
  `idproveedor` int default null,
  `idCategoria` int DEFAULT NULL,
  PRIMARY KEY (`idproducto`),
  KEY `fk_productos_Categoria1_idx` (`idCategoria`),
  CONSTRAINT `fk_productos_Categoria1` FOREIGN KEY (`idCategoria`) REFERENCES `categoria` (`idCategoria`),
  FOREIGN KEY (`idproveedor`) REFERENCES `proveedores` (`idproveedor`)
  );


CREATE TABLE `usuario` (
  `idUsuario` int NOT NULL AUTO_INCREMENT,
  `Password` varchar(45) DEFAULT NULL,
  `fecha_registro` date DEFAULT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `direccion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idUsuario`)
) ;



CREATE TABLE `transacciones` (
  `idtransaccion` int NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `idcliente` int NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `usuario_idUsuario` int NOT NULL,
  PRIMARY KEY (`idtransaccion`),
  KEY `fk_transacciones_usuario1_idx` (`usuario_idUsuario`),
  CONSTRAINT `fk_transacciones_usuario1` FOREIGN KEY (`usuario_idUsuario`) REFERENCES `usuario` (`idUsuario`)
) ;











CREATE TABLE `detalle_transaccion` (
  `iddetalle_transaccion` int NOT NULL AUTO_INCREMENT,
  `idtransaccion` int NOT NULL,
  `idproducto` int NOT NULL,
  `cantidad` int NOT NULL,
  PRIMARY KEY (`iddetalle_transaccion`),
  KEY `idtransaccion` (`idtransaccion`),
  KEY `idproducto` (`idproducto`),
  CONSTRAINT `detalle_transaccion_ibfk_1` FOREIGN KEY (`idtransaccion`) REFERENCES `transacciones` (`idtransaccion`) ON DELETE CASCADE,
  CONSTRAINT `detalle_transaccion_ibfk_2` FOREIGN KEY (`idproducto`) REFERENCES `productos` (`idproducto`)
);
















INSERT  INTO proveedores(nombre, contacto, direccion) 
VALUES ('Jose', '341766120', 'josesito'),
		('pablo', '12312312', 'cruz'),
        ('laura', '1231231','josesina');
        
INSERT  INTO categoria(idCategoria, categoria) 
VALUES (1, 'pantalones'),
		(2, 'remeras'),
        (3, 'gorras');
        
