"""
URL configuration for Proyecto3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from Proyecto3.views import saludo
from Proyecto3.views import despedida
from Proyecto3.views import damefecha
from Proyecto3.views import calculaEdad

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo), #no hace falta que se llame igual que en la funcion (el primer parametro), pero se hace por prolijidad y convencion
    path('despedida/', despedida),
    path('fecha/', damefecha),
    path('EdadEnElAgno/<int:edad>/<int:agno>', calculaEdad)
]
