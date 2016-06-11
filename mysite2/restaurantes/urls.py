from django.conf.urls import url
from .views import RegistrarRestaurante,ReportarRestaurante

from . import views


app_name = 'restaurantes'
urlpatterns = [

	url(r'^registrar/$', RegistrarRestaurante.as_view(), name="registrar_restaurante"),
	url(r'^reportar/$', ReportarRestaurante.as_view(), name="reportar_restaurante"),	
]