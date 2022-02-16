from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class Instrumento(models.Model):
    marca = models.CharField(max_length= 20)
    modelo = models.CharField(max_length = 25)
    tipoinstrumento = models.CharField(max_length = 20)
    color = models.CharField (max_length = 15)
    
    def __str__(self):
        return f"Marca: {self.marca} - Modelo: {self.modelo} - Tipo de Instrumento:{self.tipoinstrumento} - Color: {self.color}"
    
class Pedal(models.Model):
    nombre = models.CharField (max_length = 25)
    efecto = models.CharField (max_length = 15)
    bypass = models.BooleanField ()

class Discos(models.Model):
    artista = models.CharField (max_length = 35)
    album = models.CharField (max_length = 35)
    fechaLanzamiento = models.DateField()
    
    def __str__(self):
        return f"Artista: {self.artista} - Album: {self.album} - Fecha de Lanzamiento:{self.fechaLanzamiento}"

def get_image_filename(instance, filename):
    title =  'titulo'
    slug = slugify(title)
    return "imagenesAvatares/%s-%s" % (slug, filename)  

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True,blank=True)

    def __str__(self):
        return f"Imagen de: {self.user.username}"

def get_image_filename(instance, filename):
    title =  'titulo'
    slug = slugify(title)
    return "imagenesAvatares/%s-%s" % (slug, filename) 