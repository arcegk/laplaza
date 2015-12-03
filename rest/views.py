# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView , View , UpdateView , TemplateView , DetailView
import json , ast
from django.http import HttpResponse
from .models import Plato , Menu , Pedido , User , Config
from .forms import PanelDesayunosForm , PanelAlmuerzosForm
from django.core.urlresolvers import reverse, reverse_lazy
from braces.views import LoginRequiredMixin , StaffuserRequiredMixin , CsrfExemptMixin
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from geopy .distance import great_circle
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator	
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
		especial = []

		
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
			elif item.tipo == "PROTEINA":
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

			elif item.tipo == "ESPECIAL":
				especial.append({
							
				'id' : item.id ,
				'nombre' : item.nombre ,
				'tipo' : item.tipo,
				'precio' : item.precio 
				})

#		dic.append({'ESPECIAL' : especial})
		dic.append({'SOPA' : sopa})
		dic.append({'PRINCIPIO' : prin})
		dic.append({'ARROZ' : arroz})
		dic.append({'ENSALADA' : ensa})
		dic.append({'PROTEINA' : carne})
		dic.append({'ACOMPANANTE' : acom})
		dic.append({'BEBIDA' : bebida})

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

	

class PedidoApiView(APIView):

	permission_classes = (IsAuthenticated, )

	
	def get_context_data(self, **kwargs):
	    context = super(pedidoApiView, self).get_context_data(**kwargs)
	    return context

	def post(self, request):
		js = json.dumps(self.request.data)
		dta = json.loads(js)
		print dta
		data = dta['data'] 
		obj = Pedido()
		us = User.objects.get(pk=data['user'])
		obj.user = us
		if us.first_name == "generic":
			obj.nombre = data['nombre']
			
		else:
			obj.nombre = us.first_name
		
		obj.direccion = data['direccion']
		obj.empresa = data['empresa']
		obj.telefono = data['telefono']
		obj.precio = data['precio']
		obj.observaciones = data['observaciones']
		obj.estado = "PENDIENTE"
		obj.save()

		for itm in data['platos']:
			plt = Plato.objects.get(pk=itm)
			obj.orden.add(plt)

		return HttpResponse(json.dumps({'id' : obj.id }))



class UserRegisterApiView(APIView):

	def post(self, request):
		js = json.dumps(self.request.data)
		dta = json.loads(js)
		data = dta['data']
		user = User.objects.create_user(data['username'] ,
				data['email'] , 
				data['pass']  )
		user.empresa = data['empresa']
		user.token = data['token']
		user.save()

		return HttpResponse(json.dumps({'success' : True }))
		

class ReporteAPIView(APIView):

	permission_classes = (IsAdminUser, )

	def get_context_data(self, **kwargs):
		context = super(ReporteListView, self).get_context_data(**kwargs)
		return context
	
	def get(self, request):
		pedido = []
		queryset = Pedido.objects.all().exclude(estado="ENTREGADO").order_by('id')

		for item in queryset:
			pedido.append({

				'id' : item.id ,
				'nombre' : item.nombre,
				'direccion' : item.direccion,
				'telefono' : item.telefono,
				'observaciones' : item.observaciones,
				'estado' : item.estado,
				'precio' : item.precio, 

			})

		jsn = {'pedido' : pedido}
		return HttpResponse(json.dumps(jsn))



class DetalleAPIView(APIView):

	permission_classes = (IsAdminUser, )

	def post(self, request):
		js = json.dumps(self.request.data)
		dta = json.loads(js)
		ide = dta['id']
		pedido = []

		try :
			item = Pedido.objects.get(id=ide)

			for item in item.orden.all():
				pedido.append({
					'nombre': item.nombre,
					'tipo' : item.tipo,
				})


			jsn = {'pedido' : pedido}

		except ObjectDoesNotExist:
			jsn = {'success' : 'object does not exist'}

		return HttpResponse(json.dumps(jsn))




class ReporteListView(ListView):
	queryset = Pedido.objects.all().exclude(estado="ENTREGADO").order_by('id')
	template_name = 'report.html'


class HomeView(TemplateView):

	template_name = 'index.html'

class MenuAlmuerzoDetailView(DetailView):

	template_name = 'menu-almuerzo.html'

	def get_object(self):
		return Menu.objects.get(pk=2)
		

class MenuDesayunoDetailView(DetailView):

	template_name = 'menu-desayuno.html'

	def get_object(self):
		return Menu.objects.get(pk=1)

class AjaxStatusView(View):
	
	def get(self, request):
		ide = request.GET['id']
		status = request.GET['status'].upper()
		obj = Pedido.objects.get(pk=ide)
		obj.estado = status
		obj.save()
		return HttpResponse(json.dumps({'success' : True}) ,content_type='application/json')

class UpdateStatusAPIView(APIView):
	permission_classes = (IsAuthenticated, )
	
	def post(self, request):
		js = json.dumps(self.request.data)
		dta = json.loads(js)
		data = dta['data']
		obj = Pedido.objects.get(pk=data.get('id'))
		obj.estado = "ENTREGADO"
		obj.save()
		return HttpResponse(json.dumps({'success' : True}), content_type='aplication/json')

class ConfigAPIView(View):
	def get_context_data(self, **kwargs):
	    context = super(ConfigAPIView, self).get_context_data(**kwargs)
	    return context

	def get(self, request):
		tel = []
		obj = Config.objects.get(id=1)
		tel.append({"tel" : obj.telefono})
		jsn = {"data" :tel }
		return HttpResponse(json.dumps(jsn))

class CheckRangeAPIView(APIView):

	def post(self, request):
		js = json.dumps(self.request.data)
		dta = json.loads(js)
		lat = dta['lat']
		lon = dta['lon']
		p = (3.450398, -76.532919)
		dis = great_circle(p,( lat, lon ))
		print dis
		if dis < .25:
			return HttpResponse(json.dumps({'success' : True}), content_type='aplication/json')
		else:
			return HttpResponse(json.dumps({'success' : False}), content_type='aplication/json')



