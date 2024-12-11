from django.urls import path, include
from rest_framework import routers
from DressCodeApp import views

router= routers.DefaultRouter()
router.register(r'usuario', views.UsuariosViewSet)
router.register(r'producto', views.ProductosViewSet)
router.register(r'carrito', views.CarritosViewSet)
router.register(r'envio', views.EnviosViewSet)
router.register(r'pedido', views.PedidosViewSet)
router.register(r'articulos_pedido', views.ArticulosPedidoViewSet)


urlpatterns = [
    path('auth/login/', views.LoginView.as_view(), name='auth_login'),
    path('auth/logout/', views.LoginView.as_view(), name='auth_logout'),
    path('auth/register/', views.SignUpView.as_view(), name='auth_signup'),
    path('',include(router.urls)),


]