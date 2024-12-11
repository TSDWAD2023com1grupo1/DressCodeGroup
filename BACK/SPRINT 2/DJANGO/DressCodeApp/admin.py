from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ArticuloCarrito
from .models import ArticuloPedido
from .models import Carrito
from .models import Categoria
from .models import Envio
from .models import Pedido
from .models import Producto
from .models import Usuario


admin.site.register(Usuario)
admin.site.register(ArticuloCarrito)
admin.site.register(ArticuloPedido)
admin.site.register(Carrito)
admin.site.register(Categoria)
admin.site.register(Envio)
admin.site.register(Pedido)
admin.site.register(Producto)

# Register your models here.

