from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest.views import AlmuerzoView , MenuDesUpdateView , MenuAlmuerzoUpdateView ,\
    PedidoApiView , UserInfo , DesayunoView , UserRegisterApiView ,\
    BebidaView , ReporteListView , HomeView , MenuAlmuerzoDetailView , MenuDesayunoDetailView ,\
    AjaxStatusView , ReporteAPIView , UpdateStatusAPIView , ConfigAPIView , DetalleAPIView ,\
    CheckRangeAPIView

urlpatterns = patterns('',
    # Examples:
    
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
   
    url(r'^$', HomeView.as_view() , name='home'),

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
        name = 'desayunos' ) ,

    url(r'^registrar' , 
        UserRegisterApiView.as_view() ,
        name = 'register') ,

    url(r'^bebidas' ,
        BebidaView.as_view(),
        name = 'register') ,

    url(r'^reporte$' ,
        ReporteListView.as_view(),
        name="reporte"),

    url(r'^menu$' , 
        MenuAlmuerzoDetailView.as_view() ,
        name="menu-dia") ,

    url(r'^menu-desayuno$' , 
        MenuDesayunoDetailView.as_view() ,
        name="menu-desayuno") ,

    url(r'^ajax-status' , 
        AjaxStatusView.as_view() , 
        name="ajax-status"),

    url(r'^reporte_api$' , 
        ReporteAPIView.as_view() , 
        name="reporte_api"),

    url(r'^update_status$' ,
     UpdateStatusAPIView.as_view() ,
      name="update_status" ),

     url(r'^config_api$' ,
     ConfigAPIView.as_view() ,
      name="config_api" ),

     url(r'^detalle_pedido$' ,
     DetalleAPIView.as_view() ,
      name="detalle_api" ),

     url(r'^checkrange$' ,
     CheckRangeAPIView.as_view() ,
      name="checkrangekr" ),


)
