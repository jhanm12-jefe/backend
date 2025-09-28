from django.db import models

class Rol(models.Model):
    nombre = models.CharField(max_length=200)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class User(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name="usuarios")
    is_premium = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre

class Suscripcion(models.Model):
    TIPO_CHOICES = (
        ('mensual', 'Mensual'),
        ('anual', 'Anual'),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="suscripciones")
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    activa = models.BooleanField(default=True)
    metodo_pago = models.CharField(max_length=50)
    monto = models.FloatField()

    def __str__(self):
        return f"{self.usuario.nombre} - {self.tipo}"