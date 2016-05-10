# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.core.mail import EmailMultiAlternative
from django.template_loader import render_to_string
from django.views.generic import ListView , View , UpdateView , TemplateView , DetailView
import json , ast
from django.http import HttpResponse
from .models import Plato , Menu , Pedido , User , Config , Ubicacion, Combo , Venta
from .forms import PanelDesayunosForm , PanelAlmuerzosForm
from django.core.urlresolvers import reverse, reverse_lazy
from braces.views import LoginRequiredMixin , StaffuserRequiredMixin , CsrfExemptMixin
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from django.contrib.auth import authenticate
from geopy.distance import great_circle
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator	
from django.db import IntegrityError
from datetime import datetime
from serializers import ComboSerializer



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
				'precio' : item.precio,
				'extra' : item.precio_extra

							})
			elif item.tipo == "PRINCIPIO":
				prin.append({
							
				'id' : item.id ,
				'nombre' : item.nombre ,
				'tipo' : item.tipo,
				'precio' : item.precio,
				'extra' : item.precio_extra

							})
			elif item.tipo == "PROTEINA":
				carne.append({
							
				'id' : item.id ,
				'nombre' : item.nombre ,
				'tipo' : item.tipo,
				'precio' : item.precio,
				'extra' : item.precio_extra

							})

			elif item.tipo == "ENSALADA":
				ensa.append({
							
				'id' : item.id ,
				'nombre' : item.nombre ,
				'tipo' : item.tipo,
				'precio' : item.precio,
				'extra' : item.precio_extra

							})
			elif item.tipo == "BEBIDA":
				bebida.append({
							
				'id' : item.id ,
				'nombre' : item.nombre ,
				'tipo' : item.tipo,
				'precio' : item.precio,
				'extra' : item.precio_extra

							})

			elif item.tipo == "ACOMPANANTE":
				acom.append({
							
				'id' : item.id ,
				'nombre' : item.nombre ,
				'tipo' : item.tipo,
				'precio' : item.precio,
				'extra' : item.precio_extra 
				})

			elif item.tipo == "ARROZ":
				arroz.append({
							
				'id' : item.id ,
				'nombre' : item.nombre ,
				'tipo' : item.tipo,
				'precio' : item.precio,
				'extra' : item.precio_extra 
				})

			elif item.tipo == "ESPECIAL":
				especial.append({
							
				'id' : item.id ,
				'nombre' : item.nombre ,
				'tipo' : item.tipo,
				'precio' : item.precio,
				'extra' : item.precio_extra 
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
	
	def post(self , request):

		js = json.dumps(self.request.data)
		dta = json.loads(js)
		phn = dta['phone']
		try :
			usr = User.objects.get(username=phn)
			return HttpResponse(json.dumps({'success' : True, 
				'code' : usr.cod_referido}))
		except User.DoesNotExist:
			return HttpResponse(json.dumps({'success' : False}))

	

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
		try:
			us = User.objects.get(username=data['telefono'])
			obj.user = us
			obj.nombre = data['nombre']		
			obj.direccion = data['direccion']
			obj.empresa = data['empresa']
			obj.telefono = data['telefono']
			obj.precio = data['precio']
			obj.observaciones = data['observaciones']
			obj.estado = "PENDIENTE"
			if us.is_premium:
				if data['is_especial']:
					if us.credito_especial > 0:
						us.credito_especial = credito_especial - 1
						obj.cobrar = False
				else :
					if us.credito_normal > 0:
						us.credito_normal = credito_normal - 1
						obj.cobrar = False
			us.save()
			obj.save()

		except User.DoesNotExist:
			us = User.objects.get(username="generic")
			obj.user = us
			obj.nombre = data['nombre']		
			obj.direccion = data['direccion']
			obj.empresa = data['empresa']
			obj.telefono = data['telefono']
			obj.precio = data['precio']
			obj.observaciones = data['observaciones']
			obj.estado = "PENDIENTE"

		for itm in data['platos']:
			plt = Plato.objects.get(pk=itm)
			obj.orden.add(plt)

		return HttpResponse(json.dumps({'id' : obj.id }))



class UserRegisterApiView(APIView):

	def post(self, request):
		js = json.dumps(self.request.data)
		dta = json.loads(js)
		data = dta['data']
		try:
			user = User.objects.create_user(data['phone'],
					data['email'] , 
					data['pass'] ,
					)
			user.first_name = data['name']
			user.empresa = data['company']
			user.token = data['token']
			user.telefono = data['phone']
			try:
				padrino = User.objects.get(cod_referido=data['padrino'])
				user.padrino = padrino

			except User.DoesNotExist:
				user.padrino = None
			user.save()
			return HttpResponse(json.dumps({'success' : True }))
		
		except IntegrityError:
			return HttpResponse(json.dumps({'success' : False , 'type' : 'El usuario ya existe'}))
		
		

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
		obj.estado = data.get('estado').upper()
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
		obj = Ubicacion()
		obj.lat = lat
		obj.lon = lon
		obj.save()
		p = (3.450398, -76.532919)
		dis = great_circle(p,( lat, lon ))
		print dis
	#	if dis < .3:
		return HttpResponse(json.dumps({'success' : True}), content_type='aplication/json')
	#	else:
	#		return HttpResponse(json.dumps({'success' : False}), content_type='aplication/json')


class GetHistoryByPhoneAPIView(APIView):

	def post(self, request):
		js = json.dumps(self.request.data)
		dta = json.loads(js)
		phn = dta['phone']
		query = Pedido.objects.filter(telefono=phn)
		lista = []
		for item in query:
			lista.append({
				'id' : item.id ,
				'nombre' : item.nombre,
				'direccion' : item.direccion,
				'estado' : item.estado,
				'precio' : item.precio,
				'fecha' : item.fecha.strftime('%m-%d-%Y'), 
		})
		to_return = json.dumps({'success' : True, 'history' : lista})
		return HttpResponse(to_return)


class ValidatePremiumUserAPIView(APIView):

	def post(self, request):
		js = json.dumps(self.request.data)
		dta = json.loads(js)
		phn = dta['phone']
		try:
			query = User.objects.get(username=phn)
			if query.is_premium:
				return HttpResponse(json.dumps({'success' : True , 'is_premium' : True}))
			else:
				return HttpResponse(json.dumps({'success' : True , 'is_premium' : False}))

		except User.DoesNotExist:
				return HttpResponse(json.dumps({'success' : False}))


class AuthUserAPIView(APIView):

	def post(self, request):
		js = json.dumps(self.request.data)
		dta = json.loads(js)
		phn = dta['phone']
		pss = dta['pass']
		try:
			user = authenticate(username=phn, password=pss)
			if user is not None:
				return HttpResponse(json.dumps({'success' : True , 'auth' : True}))
			else:
				return HttpResponse(json.dumps({'success' : True , 'auth' : False}))
		except User.DoesNotExist:
			return HttpResponse(json.dumps({'success' : False}))


class GetReferenceAPIView(APIView):

	def post(self, request):
		js = json.dumps(self.request.data)
		dta = json.loads(js)
		phn = dta['phone']
		try:
			query = User.objects.get(username=phn)
			return HttpResponse(json.dumps({'success' : True , 
				'reference' : query.cod_referido }))
		except:
			return HttpResponse(json.dumps({'success' : False , 
				'reference' : None }))

class GetUserCreditAPIView(APIView):

	def post(self,request):
		js = json.dumps(self.request.data)
		dta = json.loads(js)
		phn = dta['phone']
		try:
			query = User.objects.get(username=phn)
			return HttpResponse(json.dumps({'success' : True , 
						'normal_credit' : query.credito_normal , 
						'especial_credit' : query.credito_especial }))
		except User.DoesNotExist:
			return HttpResponse(json.dumps({'success' : False})) 


class GetCombosView(View):

	def get(self,request):
		serializer = ComboSerializer(Combo.objects.all(), many=True)
		dit = ["Frijolada","Arroz Mixto","Arroz con pollo","Arroz Antioqueño","Arroz Cubano","Ajiaco","Mondonjo","Costilla BBQ","Sancocho de pescado","Sancocho de gallina"]
		dic = ["Sopa","Carne","Ensalada","Acompañante","Limonada"]
		return HttpResponse(json.dumps({'combos' : serializer.data,'especial' : dit ,'lunch' : dic}))


class VentaRegisterAPIView(APIView):

	def post(self, request):
		js = json.dumps(self.request.data)
		dta = json.loads(js)
		phn = dta['phone']
		combo = dta['id_combo']
		try:
			query = User.objects.get(username=phn)
			cmb = Combo.objects.get(pk=combo)
			venta = Venta.objects.create(user=query, combo=cmb)
			context = { "venta" : venta }
			html = render_to_string('email.html' , context)
			to = ['arcegk@gmail.com' , 'jose.arce.dev@gmail.com']
			email = EmailMultiAlternative("Nueva venta en restaurante plaza app" , html ,
				'Restaurante Plaza' , to)
			email.attach_alternative(html, 'text/html')
			email.send()
			return HttpResponse(json.dumps({'success': True, 'id': venta.id}))
		except User.DoesNotExist:
			return HttpResponse(json.dumps({'success': False, 'type': 'usuario no existe'}))
		except Combo.DoesNotExist:
			return HttpResponse(json.dumps({'success': False, 'type': 'combo no existe'}))
