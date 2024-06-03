from django.contrib import admin

from .models import Administrador
from .models import Categoria
from .models import DetalleTransaccion
from .models import Productos
from .models import Proveedores
from .models import Transacciones
from .models import Usuario


class AdministradorAdmin(admin.ModelAdmin):
    list_display =("idusuario", "password", "fecha_registro", "nombre", "email", "direccion")


class CategoriaAdmin(admin.ModelAdmin):
    list_display =("idcategoria", "categoria")

class DetalleTransaccionAdmin(admin.ModelAdmin):
    list_display =("iddetalle_transaccion", "idtransaccion", "idproducto", "cantidad")

class ProductosAdmin(admin.ModelAdmin):
    list_display =("idproducto", "nombre","descripcion", "precio","stock", "idproveedor","idcategoria")

class ProveedoresAdmin(admin.ModelAdmin):
    list_display =("idproveedor", "nombre", "contacto", "direccion")

class TransaccionesAdmin(admin.ModelAdmin):
    list_display =("idtransaccion", "fecha", "idcliente", "total", "usuario_idusuario")

class UsuarioAdmin(admin.ModelAdmin):
    list_display =("idusuario", "password", "fecha_registro", "nombre", "email", "direccion")


admin.site.register(Administrador, AdministradorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(DetalleTransaccion, DetalleTransaccionAdmin)
admin.site.register(Productos, ProductosAdmin)
admin.site.register(Proveedores, ProveedoresAdmin)
admin.site.register(Transacciones, TransaccionesAdmin)
admin.site.register(Usuario, UsuarioAdmin)


