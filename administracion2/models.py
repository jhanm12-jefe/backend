from django.db import models
from administracion.models import User

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Receta(models.Model):
    nombre = models.CharField(max_length=200)  # antes era TextField
    descripcion = models.TextField()
    tiempo_preparacion = models.IntegerField()
    tiempo_coccion = models.IntegerField()

    def __str__(self):
        return self.nombre




class PasoReceta(models.Model):
    receta = models.ForeignKey(Receta, related_name="pasos", on_delete=models.CASCADE)
    numero = models.IntegerField()
    descripcion = models.TextField()


class RecetaIngrediente(models.Model):
    receta = models.ForeignKey(Receta, related_name="ingredientes", on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    cantidad = models.CharField(max_length=100, default="al gusto")

    def __str__(self):
        return f"{self.cantidad} de {self.ingrediente.nombre} en {self.receta.nombre}"


class Historial(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="historial")
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    visto_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.nombre} vio {self.receta.nombre}"


class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favoritos")
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    agregado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return f"{self.usuario.nombre} {self.receta.nombre}"
