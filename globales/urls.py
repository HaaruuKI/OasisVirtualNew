from django.urls import path
from globales import views

urlpatterns = [
    path('salir/', views.close_sesion, name="close_sesion")
]