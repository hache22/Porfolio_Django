from django.urls import path
from .views import render_publicaciones, publicaciones_detalles

app_name = "blog"
urlpatterns = [
    path("", render_publicaciones, name="publicaciones"),
    path(
        "<int:publicacion_id>",
        publicaciones_detalles,
        name="detalle_publicaciones",
    ),
]
