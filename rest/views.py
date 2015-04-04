# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView , View , UpdateView , TemplateView , DetailView
import json , ast
from django.http import HttpResponse
from .models import Plato , Menu , Pedido , User
from .forms import PanelDesayunosForm , PanelAlmuerzosForm
from django.core.urlresolvers import reverse, reverse_lazy
from braces.views import LoginRequiredMixin , StaffuserRequiredMixin , CsrfExemptMixin 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from datetime import date



# Create your views here.


class AlmuerzoView(View):

	def get_context_data(self, **kwargs):
	    context = super(platosListView, self).get_context_data(**kwargs)
	    return context

	def get(self, request):
		queryset = Menu.objects.get(pk=2)
		dic = []
		sopa = []
		prin = []
		carne = []
		ensa = []
		bebida = []
		acom = []
		arroz = []

		
		for item in queryset.platos.all():
			if item.tipo == "SOPA":
				sopa.append({
							
				'id' : item.id ,
				'nombre' : item.nombre ,
				'tipo' : item.tipo,
				'precio' : item.precio

							})
			elif item.tipo == "PRINCIPIO":
				prin.append({
							
				'id' : item.id ,
				'nombre' : item.nombre ,
				'tipo' : item.tipo,
				'precio' : item.precio

							})
			elif item.tipo == "CARNE":
				carne.append({
							
				'id' : item.id ,
				'nombre' : item.nombre ,
				'tipo' : item.tipo,
				'precio' : item.precio

							})

			elif item.tipo == "ENSALADA":
				ensa.append({
							
				'id' : item.id ,
				'nombre' : item.nombre ,
				'tipo' : item.tipo,
				'precio' : item.precio

							})
			elif item.tipo == "BEBIDA":
				bebida.append({
							
				'id' : item.id ,
				'nombre' : item.nombre ,
				'tipo' : item.tipo,
				'precio' : item.precio

							})

			elif item.tipo == "ACOMPANANTE":
				acom.append({
							
				'id' : item.id ,
				'nombre' : item.nombre ,
				'tipo' : item.tipo,
				'precio' : item.precio 
				})

			elif item.tipo == "ARROZ":
				arroz.append({
							
				'id' : item.id ,
				'nombre' : item.nombre ,
				'tipo' : item.tipo,
				'precio' : item.precio 
				})

		dic.append({'SOPA' : sopa})
		dic.append({'CARNE' : carne})
		dic.append({'BEBIDA' : bebida})
		dic.append({'ENSALADA' : ensa})
		dic.append({'PRINCIPIO' : prin})
		dic.append({'ACOMPANANTE' : acom})
		dic.append({'ARROZ' : arroz})

		jsn = {'data' : dic }

		return HttpResponse(json.dumps(jsn))


class DesayunoView(View):
	def get_context_data(self, **kwargs):
	    context = super(desayunosView, self).get_context_data(**kwargs)
	    return context
	
	def get(self , request):
		queryset = Menu.objects.get(pk=1)
		dic = []
		for obj in queryset.platos.all():			
			dic.append({
			'id' : obj.id ,
			'nombre' : obj.nombre,
			'tipo' : obj.tipo ,
			'precio' : obj.precio

					})
	
		jsn = {'data' : dic }
		return HttpResponse (json.dumps(jsn))



class BebidaView(View):

	def get_context_data(self, **kwargs):
	    context = super(babidaView, self).get_context_data(**kwargs)
	    return context

	def get(self , request):

		queryset = Menu.objects.all()
		dic = []
		for itm in queryset:
			for obj in itm.platos.all() :

				if obj.tipo == "BEBIDA" :
					dic.append({

						'id' : obj.id ,
						'nombre' : obj.nombre ,
						'precio' : obj.precio 

						
					})

		jsn = {'data' : dic }

		return HttpResponse(json.dumps(jsn))


class MenuDesUpdateView(LoginRequiredMixin , StaffuserRequiredMixin, UpdateView):

	model = Menu
	form_class = PanelDesayunosForm
	template_name = 'panel_desayuno.html'
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
		return Menu.objects.get(pk=2)

class UserInfo(APIView):

	permission_classes = (IsAuthenticated,)
	


	def get(self , request):

		data ={
			'id' : request.user.id ,
			'username' : request.user.username ,

		}
		return Response(data)

	

class PedidoApiView(APIView, CsrfExemptMixin ):

	permission_classes = (IsAuthenticated, )
	
	def get_context_data(self, **kwargs):
	    context = super(pedidoApiView, self).get_context_data(**kwargs)
	    return context
	    
	@csrf_exempt
	def post(self, request):

		dta = json.loads(request.body)
		data = dta['data']
		obj = Pedido()
		obj.user = User.objects.get(pk=data['user'])
		obj.direccion = data['direccion']
		ob.empresa = data['empresa']
		obj.precio = data['precio']
		obj.telefono = data['telefono']
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


class HomeView(TemplateView):

	template_name = 'home.html'

class MenuAlmuerzoDetailView(DetailView):

	template_name = 'menu-almuerzo.html'

	def get_object(self):
		return Menu.objects.get(pk=2)
		

class MenuDesayunoDetailView(DetailView):

	template_name = 'menu-desayuno.html'

	def get_object(self):
		return Menu.objects.get(pk=1)


