from django.db import models

# Create your models here.
class ArticulosCarrito(models.Model):
    id_articulo = models.AutoField(primary_key=True)
    id_carrito = models.ForeignKey('Carritos', models.DO_NOTHING, db_column='id_carrito', blank=True, null=True)
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'articulos_carrito'

    def __str__(self):
        return "{}".format(self.id_articulo)


class ArticulosPedido(models.Model):
    id_articulo_pedido = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey('Pedidos', models.DO_NOTHING, db_column='id_pedido', blank=True, null=True)
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'articulos_pedido'

    def __str__(self):
        return "{}".format(self.id_articulo_pedido,self.id_pedido,self.id_producto,self.precio)        


class Carritos(models.Model):
    id_carrito = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carritos'

    def __str__(self):
        return "{}".format(self.id_carrito, self.fecha_creacion)


class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias'

    def __str__(self):
        return "{}".format(self.nombre_categoria)

class Envios(models.Model):
    id_envio = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey('Pedidos', models.DO_NOTHING, db_column='id_pedido', blank=True, null=True)
    direccion_envio = models.CharField(max_length=255)
    fecha_envio = models.DateTimeField(blank=True, null=True)
    estado_envio = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'envios'

    def __str__(self):
        return "{}".format(self.id_envio, self.direccion_envio)


class Pagos(models.Model):
    id_pago = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey('Pedidos', models.DO_NOTHING, db_column='id_pedido', blank=True, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(blank=True, null=True)
    metodo_pago = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'pagos'

    def __str__(self):
        return "{}".format(self.id_pago, self.monto, self.fecha_pago)

    


class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    fecha_pedido = models.DateTimeField(blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidos'

    def __str__(self):
        return "{}".format(self.id_pedido, self.fecha_pedido, self.total)


class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    imagen = models.CharField(max_length=500, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    id_categoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos'


    class Meta:
        managed = False
        db_table = 'productos'


    def __str__(self):
        return "{}".format(self.nombre_producto)


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'usuarios'

    def __str__(self):
        return "{}".format(self.nombre, self.email)