from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarMateria/', views.registrarMateria),
    path('edicionMateria/<codigo>', views.edicionMateria),
    path('editarMateria/', views.editarMateria),
    path('eliminarMateria/<codigo>', views.eliminarMateria),
]