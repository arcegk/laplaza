from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest.views import platosView , menuUpdateView , pedidoApiView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'restaurante.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
   
    url(r'^platos/' , 
    	platosView.as_view() ,
    	name="platos"),

    url(r'^panel/' , 
    	menuUpdateView.as_view() , 
    	name='panel'),

    url(r'^auth/', 
    	'rest_framework_jwt.views.obtain_jwt_token'),

    url(r'^login' ,
    	'django.contrib.auth.views.login' , 
    	{'template_name' : 'login.html'} ),

    url(r'^pedido' ,
    	pedidoApiView.as_view() , 
    	name='pedido-post' )

)
