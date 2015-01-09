from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest.views import platosView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'restaurante.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^platos/' , platosView.as_view() , name="platos"),
    url(r'^auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
)
