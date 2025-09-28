from rest_framework import serializers
from administracion2.models import Ingrediente, Receta, PasoReceta, RecetaIngrediente, Historial, Favorito
from administracion.models import User 



class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'



class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = '__all__'



class PasoRecetaSerializer(serializers.ModelSerializer):
    receta = RecetaSerializer(read_only=True)
    receta_id = serializers.PrimaryKeyRelatedField(
        queryset=Receta.objects.all(),
        source='receta',
        write_only=True
    )

    class Meta:
        model = PasoReceta
        fields = '__all__'



class RecetaIngredienteSerializer(serializers.ModelSerializer):
    receta = RecetaSerializer(read_only=True)
    receta_id = serializers.PrimaryKeyRelatedField(
        queryset=Receta.objects.all(),
        source='receta',
        write_only=True
    )

    ingrediente = IngredienteSerializer(read_only=True)
    ingrediente_id = serializers.PrimaryKeyRelatedField(
        queryset=Ingrediente.objects.all(),
        source='ingrediente',
        write_only=True
    )

    class Meta:
        model = RecetaIngrediente
        fields = '__all__'



class HistorialSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField(read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='usuario',
        write_only=True
    )

    receta = RecetaSerializer(read_only=True)
    receta_id = serializers.PrimaryKeyRelatedField(
        queryset=Receta.objects.all(),
        source='receta',
        write_only=True
    )

    class Meta:
        model = Historial
        fields = '__all__'



class FavoritoSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField(read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='usuario',
        write_only=True
    )

    receta = RecetaSerializer(read_only=True)
    receta_id = serializers.PrimaryKeyRelatedField(
        queryset=Receta.objects.all(),
        source='receta',
        write_only=True
    )

    class Meta:
        model = Favorito
        fields = '__all__'
