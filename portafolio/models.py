from django.db import models
from django.db.models.fields import CharField, URLField, DateField
from django.db.models.fields.files import ImageField
from datetime import date


class Proyecto(models.Model):
    titulo = CharField(max_length=100)
    descripcion = CharField(max_length=250)
    imagen = ImageField(upload_to="portfolio/imagenes/")
    url = URLField(blank=True)
    fecha = DateField(default=date.today)

    def __str__(self) -> str:
        return self.titulo
