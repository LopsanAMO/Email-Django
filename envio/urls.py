from django.conf.urls import url, include
from django.contrib import admin
from .views import Enviar, Home, ContactoMail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^correos/', Enviar.as_view(), name='enviar'),
    url(r'^home/', Home, name='home'),
    url(r'^contacto/', ContactoMail.as_view(), name='contacto')
]
