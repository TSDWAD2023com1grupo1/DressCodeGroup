from rest_framework import serializers
from .models import Productos
from .models import Usuarios
from .models import Carritos
from .models import Envios
from .models import Pedidos
from .models import ArticulosPedido
from .models import Pagos

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Productos
        fields="__all__"
        #fields=('nombre_producto', 'precio')


class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usuarios
        fields="__all__"
        #fields=('nombre_producto', 'precio')


class CarritosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Carritos
        fields="__all__"
        #fields=('nombre_producto', 'precio')


class EnviosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Envios
        fields="__all__"
        #fields=('nombre_producto', 'precio')


class PedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Pedidos
        fields="__all__"
        #fields=('nombre_producto', 'precio')

class ArticulosPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model= ArticulosPedido
        fields="__all__"
        #fields=('nombre_producto', 'precio')


class PagosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Pagos
        fields="__all__"
        #fields=('nombre_producto', 'precio')





