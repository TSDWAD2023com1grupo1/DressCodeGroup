from rest_framework import serializers
from .models import Usuario, Categoria, Producto, Carrito, ArticuloCarrito, Pedido, ArticuloPedido, Envio
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

def validate_password(self,value):
    return make_password(value)

Usuario = get_user_model()
# Serializer para Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True} 
        }
    def create(self,instance, validated_data):

        # Crear el usuario con los datos validados
        usuario = Usuario.objects.create_user(**validated_data)
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
        return usuario
        
    def update(self, instance, validated_data):
        # Si la contraseña es proporcionada, la actualizamos
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)  # Usa `set_password` para cifrar la contraseña

        # Actualizamos otros campos que no son la contraseña
        for attr, value in validated_data.items():
            if attr != 'password':  # No actualizar la contraseña si no ha cambiado
                setattr(instance, attr, value)

        instance.save()
        return instance



# Serializer para Categoria
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id_categoria', 'nombre_categoria', 'descripcion', 'parent_id']

# Serializer para Producto
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id_producto', 'nombre_producto', 'imagen', 'descripcion', 'precio', 'stock', 'id_categoria']

# Serializer para Carrito
class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = ['id_carrito', 'id_usuario', 'session_id', 'fecha_creacion']

# Serializer para ArticuloCarrito
class ArticuloCarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticuloCarrito
        fields = ['id_articulo', 'id_carrito', 'id_producto', 'cantidad']

# Serializer para Pedido
class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id_pedido', 'id_usuario', 'fecha_pedido', 'total', 'estado', 'metodo_pago', 'created_at', 'updated_at']

# Serializer para ArticuloPedido
class ArticuloPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticuloPedido
        fields = ['id_articulo_pedido', 'id_pedido', 'id_producto', 'cantidad', 'precio']

# Serializer para Envio
class EnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envio
        fields = ['id_envio', 'id_pedido', 'direccion_envio', 'fecha_envio', 'estado_envio']