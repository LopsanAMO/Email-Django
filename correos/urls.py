from django.conf.urls import url, include
from django.contrib import admin
from envio import urls as urlsEnvio

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^correo/', include(urlsEnvio, namespace='correo'))
]
