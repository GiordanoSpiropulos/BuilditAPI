from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Usuario.urls')),
    path('', include('Treinos.urls')),
    path('', include('Exercicios.urls'))
]
