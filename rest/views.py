from django.shortcuts import render
from django.views.generic import ListView , View
import json
from django.http import HttpResponse
from .models import Plato


# Create your views here.


class platosView(View):

	def get_context_data(self, **kwargs):
	    context = super(platosListView, self).get_context_data(**kwargs)
	    return context

	def get(request , self):
		queryset = Plato.objects.all()
		dic = [itm.as_json() for itm in queryset]
		return HttpResponse(json.dumps(dic))




	"""
	para el pedido que me envie una lista de id del producto y se hace un ciclo anadiendo
	cada vez al manytomany el objeto segun la pk

	"""