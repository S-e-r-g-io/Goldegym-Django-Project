from django.contrib import admin

from .models import Cliente, Abbonamento, Sala, Posto, Prenotazione, SubAbbonamento, FasciaOraria
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Abbonamento)
admin.site.register(Sala)
admin.site.register(Posto)
admin.site.register(Prenotazione)
admin.site.register(SubAbbonamento)
admin.site.register(FasciaOraria)
