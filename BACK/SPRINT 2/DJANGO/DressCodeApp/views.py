from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from rest_framework import viewsets
from .serializer import ProductoSerializer
from .models import Producto
from .serializer import UsuarioSerializer
from .models import Usuario
from .serializer import CarritoSerializer
from .models import Carrito
from .serializer import EnviosSerializer
from .models import Envio
from .serializer import PedidoSerializer
from .models import Pedido
from .serializer import ArticulosPedidoSerializer
from .models import ArticuloPedido




class ProductosViewSet(viewsets.ModelViewSet):
    queryset=Producto.objects.all()
    serializer_class=ProductoSerializer


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset=Usuario.objects.all()
    serializer_class=UsuarioSerializer


class CarritosViewSet(viewsets.ModelViewSet):
    queryset=Carrito.objects.all()
    serializer_class=CarritoSerializer


class EnviosViewSet(viewsets.ModelViewSet):
    queryset=Envio.objects.all()
    serializer_class=EnviosSerializer


class PedidosViewSet(viewsets.ModelViewSet):
    queryset=Pedido.objects.all()
    serializer_class=PedidoSerializer


class ArticulosPedidoViewSet(viewsets.ModelViewSet):
    queryset=ArticuloPedido.objects.all()
    serializer_class=ArticulosPedidoSerializer

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('constraseña', None)
        user = authenticate(email=email, password=password)



        if user:
            login(request, user)
            return Response(
                status=status.HTTP_200_OK
            )
        
        return Response(
            status=status.HTTP_404_NOT_FOUND
        )
    
class LogoutView(APIView):
    def post(self, request):
        logout(request)

        return Response(status=status.HTTP_200_OK)    