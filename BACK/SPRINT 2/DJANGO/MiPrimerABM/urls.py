from django.urls import path, include
from rest_framework import routers
from MiPrimerABM import views

router= routers.DefaultRouter()
router.register(r'usuarios', views.UsuariosViewSet)
router.register(r'productos', views.ProductosViewSet)
router.register(r'carritos', views.CarritosViewSet)
router.register(r'envios', views.EnviosViewSet)
router.register(r'pedidos', views.PedidosViewSet)
router.register(r'articulos_pedido', views.ArticulosPedidoViewSet)
router.register(r'pagos', views.PagosViewSet)


urlpatterns = [
    path('', include(router.urls)),
]