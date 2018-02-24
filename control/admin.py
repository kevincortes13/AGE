from django.contrib import admin
from .models import Jugador,Club,Noticias,Entrenador

class NoticiasAdmin(admin.ModelAdmin):
	list_display = ('titulo','delegacion','fecha')
	search_fields = ['futbolistas','titulo','fecha']
	list_filter = ['fecha','delegacion','futbolistas']
	date_hierarchy = 'fecha'
	readonly_fields = ('enlace',)
class JugadorAdmin(admin.ModelAdmin):
	list_display = ('nombre','apellido','posicion','club','division','created_date')
	search_fields = ['nombre','apellido','posicion','club','division']
	list_filter = ['posicion','club','division']
	date_hierarchy = 'created_date'
class EntrenadorAdmin(admin.ModelAdmin):
	list_display = ('nombre','apellido','cargo','club','division','created_date')
	search_fields = ['nombre','apellido','cargo','club','division']
	list_filter = ['cargo','club','division']
	date_hierarchy = 'created_date'
class ClubAdmin(admin.ModelAdmin):
	list_display = ('nombre_club',)
	list_filter = ['nombre_club']

admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Entrenador, EntrenadorAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Noticias, NoticiasAdmin)

# Register your models here.
