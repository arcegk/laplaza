# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView , View , UpdateView , FormView
import json , ast
from django.http import HttpResponse
from .models import Plato , Menu , Pedido , User
from .forms import PanelDesayunosForm , PanelAlmuerzosForm
from django.core.urlresolvers import reverse, reverse_lazy
from braces.views import LoginRequiredMixin , StaffuserRequiredMixin , CsrfExemptMixin 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from datetime import date



# Create your views here.


class AlmuerzoView(View):

	def get_context_data(self, **kwargs):
	    context = super(platosListView, self).get_context_data(**kwargs)
	    return context

	def get(self, request):
		queryset = Menu.objects.all()
		dic = {}
		for itm in queryset:
			for item in itm.platos.all():
				if item.seccion == "ALMUERZO" or item.tipo == "BEBIDA":
					dic.append({
						
						'id' : item.id ,
						'nombre' : item.nombre ,
						'tipo' : item.tipo,
						'precio' : item.precio

						})

		return HttpResponse(json.dumps(dic))


class DesayunoView(View):
	def get_context_data(self, **kwargs):
	    context = super(desayunosView, self).get_context_data(**kwargs)
	    return context
	
	def get(self , request):
		queryset = Menu.objects.all()
		dic = []
		for itm in queryset:
			for obj in itm.platos.all():
				if obj.seccion == "DESAYUNO" or obj.tipo == "BEBIDA":
					dic.append({
						'id' : obj.id ,
						'nombre' : obj.nombre,
						'tipo' : obj.tipo ,
						'precio' : obj.precio


						})
		return HttpResponse (json.dumps(dic))



class BebidaView(View):

	def get_context_data(self, **kwargs):
	    context = super(babidaView, self).get_context_data(**kwargs)
	    return context

	def get(self , request):

		queryset = Menu.objects.all()
		dic = {}
		for itm in queryset:
			for obj in itm.platos.all() :

				if obj.tipo == "BEBIDA" :
					dic['id'] = obj.id
					dic['nombre'] = obj.nombre
					dic['precio'] = obj.precio
						 
		return HttpResponse(json.dumps(dic))


class MenuDesUpdateView(LoginRequiredMixin , StaffuserRequiredMixin, UpdateView):

	model = Menu
	form_class = PanelDesayunosForm
	template_name = 'panel.html'
	success_url = reverse_lazy('desayunos')
	login_url = '/login'
	#lo comun de un updateview

	def get_object(self):
		return Menu.objects.get(pk=1)
		#para no tener que pasar el pk por el id le asigno uno por defecto

class MenuAlmuerzoUpdateView(LoginRequiredMixin , StaffuserRequiredMixin , UpdateView):

	model = Menu
	form_class = PanelAlmuerzosForm
	template_name = 'panel.html'
	success_url = reverse_lazy('almuerzos')
	login_url = '/login'

	def get_object(self):
		return Menu.objects.get(pk=1)

class UserInfo(APIView):

	permission_classes = (IsAuthenticated,)
	


	def get(self , request):

		data ={
			'id' : request.user.id ,
			'username' : request.user.username ,

		}
		return Response(data)

	

class PedidoApiView(APIView):

	permission_classes = (IsAuthenticated, )
	
	def get_context_data(self, **kwargs):
	    context = super(pedidoApiView, self).get_context_data(**kwargs)
	    return context

	def post(self, request):

		dta = json.loads(request.body)
		data = dta['data']
		obj = Pedido()
		obj.user = User.objects.get(pk=data['user'])
		obj.direccion = data['direccion']
		ob.empresa = data['empresa']
		obj.save()

		for itm in data['platos']:
			plt = Plato.objects.get(pk=itm)
			obj.orden.add(plt)

		return HttpResponse(json.dumps({'success' : True }))



class UserRegisterApiView(APIView):

	def post(self, request):

		dta = json.loads(request.body)
		data = dta['data']
		user = User.objects.create_user(data['username'] ,
				data['email'] , 
				data['pass']  )
		user.direccion = data['direccion']
		user.token = data['token']
		user.save()

		return HttpResponse(json.dumps({'success' : True }))
		

class ReporteListView(ListView):

	today = date.today()
	queryset = Pedido.objects.filter(fecha__contains=today).order_by('-fecha')
	template_name = 'report.html'
		



