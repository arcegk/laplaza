from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest.views import almuerzoView , menuUpdateView , pedidoApiView ,\
     userInfo , desayunoView , userRegisterApiView , bebidaView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'restaurante.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
   
    url(r'^almuerzos/' , 
    	almuerzoView.as_view() ,
    	name="almuerzos"),

    url(r'^panel/' , 
    	menuUpdateView.as_view() , 
    	name='panel'),

    url(r'^auth', 
    	'rest_framework_jwt.views.obtain_jwt_token'),

    url(r'^login' ,
    	'django.contrib.auth.views.login' , 
    	{'template_name' : 'login.html'} ),

    url(r'^pedido' ,
    	pedidoApiView.as_view() , 
    	name='pedido-post' ) ,

    url(r'^info' ,
    	userInfo.as_view() , 
    	name='info') ,

    url(r'^desayuno' ,
        desayunoView.as_view(),
        name = 'desayuno' ) ,

    url(r'^registrar' , 
        userRegisterApiView.as_view() ,
        name = 'register') ,

    url(r'^bebidas' ,
        bebidaView.as_view(),
        name = 'register') ,

)
