from django.contrib import admin
from .models import ArticulosCarrito
from .models import ArticulosPedido
from .models import Carritos
from .models import Categorias
from .models import Envios
from .models import Pagos
from .models import Pedidos
from .models import Productos
from .models import Usuarios


admin.site.register(ArticulosCarrito)
admin.site.register(ArticulosPedido)
admin.site.register(Carritos)
admin.site.register(Categorias)
admin.site.register(Envios)
admin.site.register(Pagos)
admin.site.register(Pedidos)
admin.site.register(Productos)
admin.site.register(Usuarios)
# Register your models here.

