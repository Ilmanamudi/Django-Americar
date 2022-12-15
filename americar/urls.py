from django.contrib import admin
from django.urls import path

from .views import inicio
from .views import flota
from .views import faq
from .views import testimonios
from .views import contacto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name ='inicio'),
    path('inicio/', inicio, name ='inicio'),
    path('flota/', flota, name='flota'),
    path('faq/', faq, name='faq'),
    path('testimonios/', testimonios, name='testimonios'),
    path('contacto/', contacto, name='contacto'),
]
