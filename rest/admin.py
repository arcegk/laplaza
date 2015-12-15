from django.contrib import admin

from .models import Plato , User ,Menu , Pedido , Config , Ubicacion


admin.site.register(Plato)
admin.site.register(User)
admin.site.register(Pedido)
admin.site.register(Config)
admin.site.register(Ubicacion)