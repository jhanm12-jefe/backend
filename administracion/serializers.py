from rest_framework import serializers
from .models import Rol, User, Suscripcion

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('nombre', 'correo', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        # Obtener el rol "usuario" por defecto
        rol_usuario, created = Rol.objects.get_or_create(nombre='usuario')
        validated_data['rol'] = rol_usuario
        user = User.objects.create(**validated_data)
        return user

class SuscripcionSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='usuario',
        write_only=True
    )

    class Meta:
        model = Suscripcion
        fields = '__all__'
