from django.contrib import admin
from .models import ArticulosCarrito
from .models import ArticulosPedido
from .models import Carrito
from .models import Categoria
from .models import Envio
from .models import Pago
from .models import Pedido
from .models import Producto
from .models import Usuario


admin.site.register(Usuario)
admin.site.register(ArticulosCarrito)
admin.site.register(ArticulosPedido)
admin.site.register(Carrito)
admin.site.register(Categoria)
admin.site.register(Envio)
admin.site.register(Pago)
admin.site.register(Pedido)
admin.site.register(Producto)

# Register your models here.

