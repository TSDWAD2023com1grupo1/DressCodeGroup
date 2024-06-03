from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializer import ProductosSerializer
from .models import Productos
from .serializer import UsuariosSerializer
from .models import Usuarios
from .serializer import CarritosSerializer
from .models import Carritos
from .serializer import EnviosSerializer
from .models import Envios
from .serializer import PedidosSerializer
from .models import Pedidos
from .serializer import ArticulosPedidoSerializer
from .models import ArticulosPedido
from .serializer import PagosSerializer
from .models import Pagos

class ProductosViewSet(viewsets.ModelViewSet):
    queryset=Productos.objects.all()
    serializer_class=ProductosSerializer


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset=Usuarios.objects.all()
    serializer_class=UsuariosSerializer


class CarritosViewSet(viewsets.ModelViewSet):
    queryset=Carritos.objects.all()
    serializer_class=CarritosSerializer


class EnviosViewSet(viewsets.ModelViewSet):
    queryset=Envios.objects.all()
    serializer_class=EnviosSerializer


class PedidosViewSet(viewsets.ModelViewSet):
    queryset=Pedidos.objects.all()
    serializer_class=PedidosSerializer


class ArticulosPedidoViewSet(viewsets.ModelViewSet):
    queryset=ArticulosPedido.objects.all()
    serializer_class=ArticulosPedidoSerializer

class PagosViewSet(viewsets.ModelViewSet):
    queryset=Pagos.objects.all()
    serializer_class=PagosSerializer




