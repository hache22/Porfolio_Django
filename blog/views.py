from django.shortcuts import render, get_object_or_404
from .models import Publicacion


def render_publicaciones(request):
    total_publicaciones = Publicacion.objects.count()
    publicaciones = Publicacion.objects.order_by("-fecha")
    return render(
        request,
        "blog.html",
        {"publicaciones": publicaciones, "total_publicaciones": total_publicaciones},
    )


def publicaciones_detalles(request, publicacion_id):
    publicacion = get_object_or_404(Publicacion, pk=publicacion_id)
    return render(request, "detalle_publicacion.html", {"publicacion": publicacion})
