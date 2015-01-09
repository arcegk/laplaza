from django.shortcuts import render
from django.views.generic import ListView , View , UpdateView , FormView
import json
from django.http import HttpResponse
from .models import Plato , Menu
from .forms import PanelForm
from django.core.urlresolvers import reverse, reverse_lazy
from braces.views import LoginRequiredMixin , StaffuserRequiredMixin
from rest_framework.generic import ApiView
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class platosView(View):

	def get_context_data(self, **kwargs):
	    context = super(platosListView, self).get_context_data(**kwargs)
	    return context

	def get(request , self):
		queryset = Menu.objects.all()
		dic = []
		for itm in queryset:
			for item in itm.platos.all():
				dic.append({
					
					'id' : item.id ,
					'nombre' : item.nombre ,
					'tipo' : item.tipo,

					})

		return HttpResponse(json.dumps(dic))


class menuUpdateView(LoginRequiredMixin , StaffuserRequiredMixin, UpdateView):

	model = Menu
	form_class = PanelForm
	template_name = 'panel.html'
	success_url = reverse_lazy('platos')
	login_url = '/login'
	#lo comun de un updateview

	def get_object(self):
		return Menu.objects.get(pk=1)
		#para no tener que pasar el pk por el id le asigno uno por defecto

	

class pedidoApiView(ApiView):

	permission_classes = (IsAuthenticated, )

	def post(request, self):

		data = json.loads(request.POST['data'])
		obj = Pedido()
		obj.user = User.object.get(pk=data.user)
		obj.arroz = data.arroz
		obj.ensalada = data.ensalada
		obj.save()

		for itm in data.platos:
			plt = Plato.objects.get(pk=itm)
			obj.orden.add(plt)

		return HttpResponse(json.dumps({'success' : True }))



		



