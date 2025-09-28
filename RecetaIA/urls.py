"""
URL configuration for recetaia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from administracion.views import (
    crudSuscripcion,
    crudSuscripcion_detail,
    prueba,
    crudRol,
    crudRol_detail,
    crudUser,
    crudUser_detail,
    loginUser,
    showByRol,
)

from administracion2.views import (
    agregar_favorito,
    crudIngrediente,
    crudIngrediente_detail,
    crudReceta,
    crudReceta_detail,
    crudPasoReceta,
    crudPasoReceta_detail,
    crudRecetaIngrediente,
    crudRecetaIngrediente_detail,
    crudHistorial,
    crudHistorial_detail,
    crudFavorito,
    crudFavorito_detail,
)
from ia.views import  detalle_receta, generar_receta
#from ia.views import chatia

urlpatterns = [
    path('admin/', admin.site.urls),

    # Prueba y IA
    path('prueba/', prueba),
    #path('ia/', chatia),

    # Roles
    path('rol/', crudRol),
    path('rol/<int:id>/', crudRol_detail),

    # Usuarios
    path('user/', crudUser, name='crud_user'),
    path('user/<int:id>/', crudUser_detail, name='crud_user_detail'),
    path('user/rol/<int:id>/', showByRol, name='user_by_rol'),

    # Suscripciones
    path('suscripcion/', crudSuscripcion),
    path('suscripcion/<int:id>/', crudSuscripcion_detail),

    # Ingredientes y recetas
    path('ingrediente/', crudIngrediente),
    path('ingrediente/<int:id>/', crudIngrediente_detail),
    path('receta/', crudReceta),
    path('receta/<int:id>/', crudReceta_detail),
    path('paso/', crudPasoReceta),
    path('paso/<int:id>/', crudPasoReceta_detail),
    path('receta-ingrediente/', crudRecetaIngrediente),
    path('receta-ingrediente/<int:id>/', crudRecetaIngrediente_detail),

    # Historial y favoritos
    path('historial/', crudHistorial),
    path('historial/<int:id>/', crudHistorial_detail),
    path('favorito/', crudFavorito),
    path('favorito/<int:id>/', crudFavorito_detail),

    # Login
    path("api/login/", loginUser, name="api-login"),
    
    
    # IA
    path("ia/generar/", generar_receta),
    path("ia/detalle/<int:receta_id>/", detalle_receta),
    path("ia/favorito/<int:receta_id>/", agregar_favorito),
]
