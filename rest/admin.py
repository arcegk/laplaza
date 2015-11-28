from django.contrib import admin

from .models import Plato , User ,Menu , Pedido , Config


admin.site.register(Plato)
admin.site.register(User)
admin.site.register(Pedido)
admin.site.register(Config)
