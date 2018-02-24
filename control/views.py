from urllib.parse import quote
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Club,Jugador,Noticias,Entrenador
from django.shortcuts import render, get_object_or_404 
from django.shortcuts import redirect
from django.utils.safestring import mark_safe

def post_list_jugadores(request):
	player = Jugador.objects.all()
	return render(request, 'elite/jugadores.html', {'player':player})

def list_entrenadores(request):
	coach = Entrenador.objects.all()
	return render(request, 'elite/entrenadores.html', {'coach':coach})

def post_list_jugadores_busquedad(request, pk):
	# player = get_object_or_404(Jugador,pk=pk)
	if pk == Jugador.DELANTERO:
		player = Jugador.objects.filter(posicion=Jugador.DELANTERO)
	elif pk == Jugador.MEDIO:
		player = Jugador.objects.filter(posicion=Jugador.MEDIO)
	elif pk == Jugador.DEFENSA:
		player = Jugador.objects.filter(posicion=Jugador.DEFENSA)
	elif pk == Jugador.PORTERO:
		player = Jugador.objects.filter(posicion=Jugador.PORTERO)
	else:
		player = Jugador.objects.all()
	return render(request, 'elite/jugadores.html', {'player':player})

def post_index(request):
	player = Jugador.objects.all()[:12]
	noticia = Noticias.objects.all()[:2]
	return render(request, 'elite/index.html', {'player':player,'noticia':noticia})

def marketing(request):
	player = Jugador.objects.all()
	return render(request, 'elite/marketing.html', {'player':player})

def contacto(request):
	player = Jugador.objects.all()
	return render(request, 'elite/contacto.html', {'player':player})
def equipo_tecnico(request):
	player = Jugador.objects.all()
	return render(request, 'elite/equipo.html', {'player':player})
def servicios(request):
	player = Jugador.objects.all()
	return render(request, 'elite/servicio.html', {'player':player})
def empresa(request):
	player = Jugador.objects.all()
	return render(request, 'elite/empresa.html', {'player':player})
def areas_de_influencias(request):
	player = Jugador.objects.all()
	return render(request, 'elite/areas-de-influencias.html', {'player':player})
def nosotros(request):
	player = Jugador.objects.all()
	return render(request, 'elite/nosotros.html', {'player':player})
def get_noticias(request):
	noticia_list = Noticias.objects.all()
	paginator = Paginator(noticia_list, 5) # Show 5 news per page
	page = request.GET.get('p')

	try:
		noticia = paginator.page(page)
	except PageNotAnInteger:
		noticia = paginator.page(1)
	except EmptyPage:
		noticia = paginator.page(paginator.num_pages)

	return render(request, 'elite/noticias.html', {'noticia':noticia})

def get_noticias_detail(request,pk):
	# try:
	# 	print(pk)
	# 	nota = Noticias.objects.get(enlace=pk)
	# except Noticias.DoesNotExist:
	# 	raise Http404("News does not exist")
	nota = get_object_or_404(Noticias, enlace=pk)

	texto = ''
	sw = False
	for x in range(0,len(nota.contenido)):
		if nota.contenido[x] == '<':
			sw = True
		elif sw == False:
			texto += nota.contenido[x]
		elif nota.contenido[x] == '>':
			sw = False

	print('texto: '+texto)
	sharen_string = quote(texto)
	print(sharen_string)
	sharen_titulo = quote(nota.titulo)
	return render(request, 'elite/noticias_detail.html', {'noticia':nota,'sharen_string':sharen_string,'sharen_titulo':sharen_titulo})

# Create your views here.
