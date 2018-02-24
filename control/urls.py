from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.post_index, name='post_index'),
    url(r'^jugadores/$', views.post_list_jugadores, name='post_list_jugadores'),
    url(r'^jugadores/(?P<pk>[-\w]+)/$', views.post_list_jugadores_busquedad, name='post_list_jugadores_busquedad'),
    url(r'^entrenadores/$', views.list_entrenadores, name='list_entrenadores'),
    url(r'^marketing/$', views.marketing, name='marketing'),
    url(r'^contacto/$', views.contacto, name='contacto'),
    url(r'^noticias/$', views.get_noticias, name='get_noticias'),
    url(r'^empresa/$', views.empresa, name='empresa'),
    url(r'^noticias/(?P<pk>[-\w]+)/$', views.get_noticias_detail, name='get_noticias_detail'),
    url(r'^empresa/equipo-tecnico/$', views.equipo_tecnico, name='equipo_tecnico'),
    url(r'^empresa/servicios/$', views.servicios, name='servicios'),
    url(r'^empresa/areas-de-influencias/$', views.areas_de_influencias, name='areas_de_influencias'),
    url(r'^empresa/nosotros/$', views.nosotros, name='nosotros'),
    url(r'^tinymce/', include('tinymce.urls')),

]