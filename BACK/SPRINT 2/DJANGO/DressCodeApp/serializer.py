from rest_framework import serializers
from .models import Producto
from .models import Usuario
from .models import Carrito
from .models import Envio
from .models import Pedido
from .models import ArticuloPedido


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Producto
        fields="__all__"
        #fields=('nombre_producto', 'precio')


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usuario
        fields="__all__"
        #fields=('nombre_producto', 'precio')


class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Carrito
        fields="__all__"
        #fields=('nombre_producto', 'precio')


class EnviosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Envio
        fields="__all__"
        #fields=('nombre_producto', 'precio')


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Pedido
        fields="__all__"
        #fields=('nombre_producto', 'precio')

class ArticulosPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model= ArticuloPedido
        fields="__all__"
        #fields=('nombre_producto', 'precio')




