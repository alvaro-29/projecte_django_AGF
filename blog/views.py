from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag
from datetime import date
from django.utils.timezone import now

# Aquí definim les vistes que gestionen el comportament de les diferents pàgines del blog.

def starting_page(request):
    """Renderitza la pàgina inicial del blog amb els tres posts més recents."""
    # Obtenim tots els posts i els ordenem per data descendent; agafem només els tres primers.
    latest_posts = Post.objects.all().order_by("-date")[:3]
    # Renderitzem la plantilla 'index.html' passant-li els posts recents.
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    """Mostra una llista de tots els posts del blog ordenats per data descendent."""
    # Obtenim tots els posts i els ordenem per data descendent.
    all_posts = Post.objects.all().order_by("-date")
    # Renderitzem la plantilla 'posts.html' amb tots els posts.
    return render(request, "blog/posts.html", {"posts": all_posts})


def post_detail(request, slug):
    """Mostra els detalls d'un post concret identificat pel seu slug."""
    # Cerquem un post concret pel seu slug; si no existeix, retornem error 404.
    post = get_object_or_404(Post, slug=slug)
    # Renderitzem la plantilla amb el detall del post.
    return render(request, "blog/post-detail-page.html", {"post": post})


def autors(request):
    """Mostra una llista de tots els autors del blog."""
    # Obtenim tots els autors de la base de dades.
    autors = Author.objects.all()
    # Renderitzem la plantilla 'autors.html' amb la llista d'autors.
    return render(request, "blog/autors.html", {"autors": autors})


def author_detail(request, id):
    """Mostra els detalls d'un autor concret identificat pel seu ID."""
    # Cerquem un autor pel seu ID; si no existeix, retornem error 404.
    autor = get_object_or_404(Author, id=id)
    # Renderitzem la plantilla amb el detall de l'autor.
    return render(request, "blog/author-detail-page.html", {"author": autor})


def tags(request):
    """Mostra una llista de totes les etiquetes (tags) disponibles al blog."""
    # Obtenim totes les etiquetes de la base de dades.
    tags = Tag.objects.all()
    # Renderitzem la plantilla 'tags.html' amb la llista d'etiquetes.
    return render(request, "blog/tags.html", {"tags": tags})


def tag_detail(request, slug):
    """Mostra els detalls d'una etiqueta concreta i tots els posts associats a aquesta."""
    # Cerquem una etiqueta pel seu slug; si no existeix, retornem error 404.
    tag = get_object_or_404(Tag, slug=slug)
    # Obtenim tots els posts que tenen associada aquesta etiqueta.
    all_posts = Post.objects.filter(tags=tag)
    # Renderitzem la plantilla amb el detall de l'etiqueta i els seus posts relacionats.
    return render(request, "blog/tag-detail-page.html", {"tag": tag, "posts": all_posts})