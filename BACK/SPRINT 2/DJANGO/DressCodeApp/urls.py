from django.urls import path, include
from rest_framework import routers
from DressCodeApp import views

router= routers.DefaultRouter()
router.register(r'usuarios', views.UsuariosViewSet)
router.register(r'productos', views.ProductosViewSet)
router.register(r'carritos', views.CarritosViewSet)
router.register(r'envios', views.EnviosViewSet)
router.register(r'pedidos', views.PedidosViewSet)
router.register(r'articulos_pedido', views.ArticulosPedidoViewSet)


urlpatterns = [
    path('auth/login/', views.LoginView.as_view(), name='auth_login'),
    path('auth/logout/', views.LoginView.as_view(), name='auth_logout'),
    
]