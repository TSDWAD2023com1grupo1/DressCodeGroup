from django.db import models
from django.contrib.auth.models import AbstractUser

# Modelo Usuario
class Usuario(AbstractUser):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    rol = models.CharField(max_length=20, choices=[('cliente', 'Cliente'), ('administrador', 'Administrador')], default='cliente')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    class Meta:
        managed = False
        db_table = 'usuario'

    def __str__(self):
        return f"{self.nombre} ({self.email})"


# Modelo Categoria
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    parent_id = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, related_name='subcategorias')

    class Meta:
        managed = False
        db_table = 'categoria'

    def __str__(self):
        return self.nombre_categoria


# Modelo Producto
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    imagen = models.CharField(max_length=500, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_categoria')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'producto'

    def __str__(self):
        return self.nombre_producto


# Modelo Carrito
class Carrito(models.Model):
    id_carrito = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_usuario')
    session_id = models.CharField(max_length=255, unique=True, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'carrito'

    def __str__(self):
        return f"Carrito {self.id_carrito} del usuario {self.id_usuario}"


# Modelo ArticuloCarrito
class ArticuloCarrito(models.Model):
    id_articulo = models.AutoField(primary_key=True)
    id_carrito = models.ForeignKey(Carrito, models.DO_NOTHING, db_column='id_carrito')
    id_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_producto')
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'articulo_carrito'

    def __str__(self):
        return f"Artículo {self.id_articulo} en carrito {self.id_carrito}"


# Modelo Pedido
class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_usuario')
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('completado', 'Completado'), ('cancelado', 'Cancelado')], default='pendiente')
    metodo_pago = models.CharField(max_length=20, choices=[('tarjeta_credito', 'Tarjeta de Crédito'), ('paypal', 'PayPal'), ('transferencia', 'Transferencia')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'pedido'

    def __str__(self):
        return f"Pedido {self.id_pedido} del usuario {self.id_usuario}"


# Modelo ArticuloPedido
class ArticuloPedido(models.Model):
    id_articulo_pedido = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='id_pedido')
    id_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_producto')
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'articulo_pedido'

    def __str__(self):
        return f"Artículo {self.id_articulo_pedido} en pedido {self.id_pedido}"


# Modelo Envio
class Envio(models.Model):
    id_envio = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='id_pedido')
    direccion_envio = models.CharField(max_length=255)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    estado_envio = models.CharField(max_length=20, choices=[('preparando', 'Preparando'), ('enviado', 'Enviado'), ('entregado', 'Entregado')], default='preparando')

    class Meta:
        managed = False
        db_table = 'envio'

    def __str__(self):
        return f"Envío {self.id_envio} para pedido {self.id_pedido}"