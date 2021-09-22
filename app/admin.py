from django.contrib import admin
from .models import Hraci, Servery, Bany, Bugy, Moderovani, Typy_banu, Typy_bugu, Formulare #Importujeme si modely

#Modely registrujeme
admin.site.register(Hraci)
admin.site.register(Servery)
admin.site.register(Bany)
admin.site.register(Bugy)
admin.site.register(Moderovani)
admin.site.register(Typy_banu)
admin.site.register(Typy_bugu)
admin.site.register(Formulare)