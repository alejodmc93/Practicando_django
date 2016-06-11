from django.views.generic import CreateView,TemplateView
from .models import Restaurate
from django.core.urlresolvers import reverse_lazy


class RegistrarRestaurante(CreateView):
	template_name = 'restaurantes/registrar.html'
	fields="__all__"
	model = Restaurate
	success_url = reverse_lazy('reportar_restaurante')

class ReportarRestaurante(TemplateView):
	template_name = 'restaurantes/reportar.html'	