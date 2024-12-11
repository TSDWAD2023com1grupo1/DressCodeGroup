
-- Insertar datos en la tabla de Categorías
INSERT INTO categoria (nombre_categoria, descripcion, parent_id)
VALUES 
('Ropa', 'Prendas de vestir en general', NULL),
('Accesorios', 'Complementos como bolsos, joyas, etc.', 1),
('Zapatos', 'Calzado para todo tipo de ocasiones', NULL);

-- Insertar datos en la tabla de Usuarios
INSERT INTO usuario (nombre, email, password, direccion, telefono, rol)
VALUES 
('Juan Pérez', 'juan.perez@example.com', 'password123', 'Calle Falsa 123', '1234567890', 'usuario'),
('María López', 'maria.lopez@example.com', 'password456', 'Avenida Siempre Viva 456', '0987654321', 'administrador');

-- Insertar datos en la tabla de Productos
INSERT INTO producto (nombre_producto, imagen, descripcion, precio, stock, id_categoria)
VALUES
('Remera <Code>','https://raw.githubusercontent.com/JavierCarranza0101/imagenes-dresscodehost/main/imagenes/remera_code.jpeg','Expresa tu amor por la programación con nuestra Camiseta code en letras verdes sobre negro! ',25000.00,15,1),
('Pantalon Binario','https://raw.githubusercontent.com/JavierCarranza0101/imagenes-dresscodehost/main/imagenes/pantalon_binario.jpeg','¡Eleva tu estilo al siguiente nivel con nuestros Pantalones Binarios!',30000.00,15,1),
('Taza The CodeFather','https://raw.githubusercontent.com/JavierCarranza0101/imagenes-dresscodehost/main/imagenes/taza_father.jpeg',' Presentamos "The Code Father" en nuestra exclusiva Taza Negra con letras blancas y un toque de estilo "El Padrino". Esta taza rinde homenaje al legendario "El Padrino" pero con un giro tecnológico.',15000.00,15,2),
('Mochila Code','https://raw.githubusercontent.com/JavierCarranza0101/imagenes-dresscodehost/main/imagenes/mochila_code.jpeg','¡Lleva tu amor por la programación a todas partes con nuestra mochila',40000.00,15,2),
('Gorra Dev','https://raw.githubusercontent.com/JavierCarranza0101/imagenes-dresscodehost/main/imagenes/gorra_dev.jpeg','¡Lleva tu pasión por el desarrollo a otro nivel con nuestra exclusiva Gorra "DEV" en blanco sobre negro! La gorra presenta un diseño elegante y minimalista en color negro que se adapta a cualquier atuendo, desde casual hasta más formal. Cuenta con un diseño contemporáneo que incorpora la palabra "DEV" en blanco, destacando tu amor por el desarrollo y la programación.',20000.00,15,2),
('Remera <Delete>','https://raw.githubusercontent.com/JavierCarranza0101/imagenes-dresscodehost/main/imagenes/remera_delete.jpeg','¿Estás listo para hacer una declaración audaz y un poco irreverente? ¡Nuestra Camiseta "delete" es la elección perfecta!',25000.00,15,1),
('Remera <NULL>','https://raw.githubusercontent.com/JavierCarranza0101/imagenes-dresscodehost/main/imagenes/remera_null.jpeg','¡Haz una declaración de estilo y programación con nuestra Camiseta "null"!Esta camiseta es perfecta para aquellos que aprecian la simplicidad y tienen un amor por la codificación.',25000.00,15,1),
('Taza Idiot','https://raw.githubusercontent.com/JavierCarranza0101/imagenes-dresscodehost/main/imagenes/taza_idiot.jpeg','¡Añade un toque de humor y reflexión a tus mañanas con nuestra Taza "El Ciclo Interminable".',15000.00,15,2),
('Gorra <Head>','https://raw.githubusercontent.com/JavierCarranza0101/imagenes-dresscodehost/main/imagenes/gorra_head.jpeg','¡Lleva la esencia del mundo digital a tu estilo con nuestra exclusiva Gorra en blanco sobre negro! Esta gorra es un tributo a la programación web y al elemento fundamental  que inicia cada página web.',20000.00,15,2);

-- Insertar datos en la tabla de Carritos
INSERT INTO carrito (id_usuario, session_id)
VALUES 
(1, 'session_juan123'),
(2, 'session_maria456');

-- Insertar datos en la tabla de Artículos en el Carrito
INSERT INTO articulo_carrito (id_carrito, id_producto, cantidad)
VALUES 
(1, 1, 2), -- Juan Pérez añade 2 camisetas
(1, 2, 1), -- Juan Pérez añade 1 bolso
(2, 3, 1); -- María López añade 1 par de zapatillas

-- Insertar datos en la tabla de Pedidos
INSERT INTO pedido (id_usuario, total, estado, metodo_pago)
VALUES 
(1, 59.97, 'pendiente', 'tarjeta_credito'),
(2, 79.99, 'pendiente', 'paypal');

-- Insertar datos en la tabla de Artículos en el Pedido
INSERT INTO articulo_pedido (id_pedido, id_producto, cantidad, precio)
VALUES 
(1, 1, 2, 19.99), -- Juan Pérez compra 2 camisetas
(1, 2, 1, 49.99), -- Juan Pérez compra 1 bolso
(2, 3, 1, 79.99); -- María López compra 1 par de zapatillas

-- Insertar datos en la tabla de Envíos
INSERT INTO envio (id_pedido, direccion_envio, estado_envio)
VALUES 
(1, 'Calle Falsa 123', 'preparando'),
(2, 'Avenida Siempre Viva 456', 'preparando');