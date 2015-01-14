from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest.views import AlmuerzoView , MenuDesUpdateView , MenuAlmuerzoUpdateView ,\
    PedidoApiView , UserInfo , DesayunoView , UserRegisterApiView ,\
    BebidaView , ReporteListView 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'restaurante.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
   
    url(r'^almuerzos/' , 
    	AlmuerzoView.as_view() ,
    	name="almuerzos"),

    url(r'^panel/desayunos' , 
    	MenuDesUpdateView.as_view() , 
    	name='panel-desayunos'),

    url(r'^panel/almuerzos' ,
        MenuAlmuerzoUpdateView.as_view() ,
        name = 'panel-almuerzos') ,

    url(r'^auth', 
    	'rest_framework_jwt.views.obtain_jwt_token'),

    url(r'^login' ,
    	'django.contrib.auth.views.login' , 
    	{'template_name' : 'login.html'} ),

    url(r'^pedido' ,
    	PedidoApiView.as_view() , 
    	name='pedido-post' ) ,

    url(r'^info' ,
    	UserInfo.as_view() , 
    	name='info') ,

    url(r'^desayuno' ,
        DesayunoView.as_view(),
        name = 'desayuno' ) ,

    url(r'^registrar' , 
        UserRegisterApiView.as_view() ,
        name = 'register') ,

    url(r'^bebidas' ,
        BebidaView.as_view(),
        name = 'register') ,

    url(r'^reporte' ,
        ReporteListView.as_view(),
        name="reporte")
)
