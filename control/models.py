from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField


class Club(models.Model):
	nombre_club=models.CharField(max_length=40, verbose_name='Club')
	logo_club=models.ImageField(upload_to='club/',
		null=True, 
		blank=True,
		verbose_name='Logo del Club')
	def __str__(self):
		return str(self.nombre_club)
	class Meta:
		ordering = ['nombre_club']

def upload_location(instance, filename):
	filebase, extension = filename.split('.')
	return '%s/%s.%s' %(instance.id, instance.id, extension)

class Jugador(models.Model):
	id_j=models.AutoField(primary_key=True)
	nombre=models.CharField(max_length=40)
	apellido=models.CharField(max_length=40)
	fecha_nacimiento=models.DateField(auto_now=False, auto_now_add=False)
	nacionalidad=models.CharField(max_length=40,verbose_name='Nacionalidad')
	DELANTERO='delanteros'
	MEDIO='centrocampistas'
	DEFENSA='defensas'
	PORTERO='porteros'
	POSICION_CHOICES=((PORTERO,'Portero'),(DEFENSA,'Defensa'),(MEDIO,'CentroCampista'),(DELANTERO,'Delantero'))
	posicion=models.CharField(max_length=15,choices=POSICION_CHOICES)
	div=(('primera','1era Division'),('segunda','2da Division'),('tercera','3ra Division'))
	division=models.CharField(max_length=7,choices=div)
	# Fields OneToMany Un equipo puede tener varios jugadores, un jugador un solo equipo
	club=models.ForeignKey(Club, related_name='c', null=True, blank=True) 
	imagen=models.ImageField(upload_to='jugadores/',
		null=True, 
		blank=True,
		verbose_name='Imagen')
	link=models.URLField(max_length=200)
	created_date = models.DateTimeField(
          auto_now=True, auto_now_add=False)

	def __str__(self):
		return str(self.nombre+' '+self.apellido)
	# Ordenar mis modelos
	class Meta:
		ordering = ['-id_j']

class Entrenador(models.Model):
	id_e=models.AutoField(primary_key=True)
	nombre=models.CharField(max_length=40)
	apellido=models.CharField(max_length=40)
	fecha_nacimiento=models.DateField(auto_now=False, auto_now_add=False)
	nacionalidad=models.CharField(max_length=40,verbose_name='Nacionalidad')
	ENTRENADOR='entrenador'
	CARGO_CHOICES=(('vacio',' '),(ENTRENADOR,'Entrenador'))
	cargo=models.CharField(max_length=15,choices=CARGO_CHOICES)
	div=(('primera','1era Division'),('segunda','2da Division'),('tercera','3ra Division'))
	division=models.CharField(max_length=7,choices=div)
	# Fields OneToMany Un equipo puede tener varios jugadores, un jugador un solo equipo
	club=models.ForeignKey(Club, related_name='c_entrenador', null=True, blank=True) 
	imagen=models.ImageField(upload_to='entrenadores/',
		null=True, 
		blank=True,
		verbose_name='Imagen')
	created_date = models.DateTimeField(
          auto_now=True, auto_now_add=False)

	def __str__(self):
		return str(self.nombre+' '+self.apellido)
	# Ordenar mis modelos
	class Meta:
		ordering = ['-id_e']

class Noticias(models.Model):
	id_n=models.AutoField(primary_key=True)
	titulo=models.CharField(max_length=200)
	
	enlace=models.SlugField(unique=True)
	contenido = HTMLField('Contenido')
	fecha=models.DateField(auto_now=False, auto_now_add=False)
	imagen_noticia=models.ImageField(upload_to='noticias/',
		null=True, 
		blank=True,
		verbose_name='Imagen de la Noticia')
	OCCIDENTAL='occidental'
	CENTRAL='central'
	ORIENTAL='oriental'
	INTERNACIONAL='internacional'
	deleg=((OCCIDENTAL,'GrupoElite Occidental'),(CENTRAL,'GrupoElite Central'),(ORIENTAL,'GrupoElite Oriental'),(INTERNACIONAL,'GrupoElite Internacional'))
	delegacion=MultiSelectField(choices=deleg)
	futbolistas=models.ManyToManyField(Jugador,null=True,blank=True)
	fecha_creado=models.DateTimeField(auto_now=True, auto_now_add=False)

	# enlace=AutoSlugField(populate_from=lambda instance: instance.titulo, unique_with=['fecha_publicado__year'], slugify=lambda value: value.replace(' ','-'))
	def __str__(self):
		return str(self.titulo)

	def save(self, *args, **kwargs):
		self.enlace = slugify(self.titulo)
		super(Noticias, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse("post:detail", kwargs={"enlace": self.enlace})
	class Meta:
		ordering = ['-fecha']