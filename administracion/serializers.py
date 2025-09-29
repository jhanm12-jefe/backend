from rest_framework import serializers
from django.contrib.auth.hashers import make_password
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
        # Hashear la contraseña antes de crear
        password = validated_data.pop('password')
        rol_usuario, _ = Rol.objects.get_or_create(nombre='usuario')
        user = User(**validated_data)
        user.password = make_password(password)
        user.rol = rol_usuario
        user.save()
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

    def create(self, validated_data):
        # Crear la suscripción normalmente
        suscripcion = super().create(validated_data)

        # Actualizar al usuario como premium
        usuario = suscripcion.usuario
        usuario.is_premium = True
        usuario.save()

        return suscripcion

    def update(self, instance, validated_data):
        # Actualizar la suscripción
        suscripcion = super().update(instance, validated_data)

        # Mantener coherencia: si la suscripción está activa => premium
        usuario = suscripcion.usuario
        usuario.is_premium = suscripcion.activa
        usuario.save()

        return suscripcion