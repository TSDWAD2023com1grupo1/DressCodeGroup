-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS dresscode_3;
USE dresscode_3;

-- Tabla de Categorías
CREATE TABLE categoria (
  id_categoria INT NOT NULL AUTO_INCREMENT,
  nombre_categoria VARCHAR(100) NOT NULL,
  descripcion TEXT,
  parent_id INT DEFAULT NULL,
  PRIMARY KEY (id_categoria),
  FOREIGN KEY (parent_id) REFERENCES categoria(id_categoria)
);

-- Tabla de Usuarios
CREATE TABLE usuario (
  id_usuario INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  direccion VARCHAR(255),
  telefono VARCHAR(20),
  rol ENUM('usuario', 'administrador') DEFAULT 'usuario',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id_usuario)
);

-- Tabla de Productos
CREATE TABLE producto (
  id_producto INT NOT NULL AUTO_INCREMENT,
  nombre_producto VARCHAR(100) NOT NULL,
  imagen VARCHAR(500),
  descripcion LONGTEXT,
  precio DECIMAL(10,2) NOT NULL,
  stock INT NOT NULL,
  id_categoria INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id_producto),
  FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
);

-- Tabla de Carritos
CREATE TABLE carrito (
  id_carrito INT NOT NULL AUTO_INCREMENT,
  id_usuario INT NOT NULL,
  session_id VARCHAR(255) UNIQUE,
  fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id_carrito),
  FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);

-- Tabla de Artículos en el Carrito
CREATE TABLE articulo_carrito (
  id_articulo INT NOT NULL AUTO_INCREMENT,
  id_carrito INT NOT NULL,
  id_producto INT NOT NULL,
  cantidad INT NOT NULL,
  PRIMARY KEY (id_articulo),
  FOREIGN KEY (id_carrito) REFERENCES carrito(id_carrito),
  FOREIGN KEY (id_producto) REFERENCES producto(id_producto)
);

-- Tabla de Pedidos
CREATE TABLE pedido (
  id_pedido INT NOT NULL AUTO_INCREMENT,
  id_usuario INT NOT NULL,
  fecha_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  total DECIMAL(10,2) NOT NULL,
  estado ENUM('pendiente', 'completado', 'cancelado') DEFAULT 'pendiente',
  metodo_pago ENUM('tarjeta_credito', 'paypal', 'transferencia') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id_pedido),
  FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);

-- Tabla de Artículos en el Pedido
CREATE TABLE articulo_pedido (
  id_articulo_pedido INT NOT NULL AUTO_INCREMENT,
  id_pedido INT NOT NULL,
  id_producto INT NOT NULL,
  cantidad INT NOT NULL,
  precio DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (id_articulo_pedido),
  FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido),
  FOREIGN KEY (id_producto) REFERENCES producto(id_producto)
);

-- Tabla de Envíos
CREATE TABLE envio (
  id_envio INT NOT NULL AUTO_INCREMENT,
  id_pedido INT NOT NULL,
  direccion_envio VARCHAR(255) NOT NULL,
  fecha_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  estado_envio ENUM('preparando', 'enviado', 'entregado') DEFAULT 'preparando',
  PRIMARY KEY (id_envio),
  FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido)
);


