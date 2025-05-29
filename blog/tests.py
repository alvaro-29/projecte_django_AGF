from django.test import TestCase
from blog.models import Author, Tag, Post
from django.test import TestCase
from django.urls import reverse
from blog.models import Post, Author, Tag

# Create your tests here.

# Test per al model Author
class AuthorModelTest(TestCase):
    def test_str_representation(self):
        # Comprovem que el mètode __str__ d'un autor retorna el nom i cognom correctament
        author = Author(nom="Anna", cognom="Serra", email_address="anna@example.com")
        self.assertEqual(str(author), "Anna Serra")

# Test per al model Tag
class TagModelTest(TestCase):
    def test_str_representation(self):
        # Comprovem que el mètode __str__ d'una etiqueta retorna el caption correctament
        tag = Tag(caption="Tecnologia", slug="tecnologia")
        self.assertEqual(str(tag), "Tecnologia")

# Test per al model Post
class PostModelTest(TestCase):

    def setUp(self):
        # Configurem les dades prèvies per als tests: un autor i una etiqueta
        self.author = Author.objects.create(
            nom="Pau", cognom="Martí", email_address="pau@example.com"
        )
        self.tag = Tag.objects.create(caption="Ciència", slug="ciencia")

    def test_str_representation(self):
        # Creem un post i associem-hi l'autor i l'etiqueta
        post = Post.objects.create(
            title="Post de prova",
            excerpt="Resum curt",
            img_name="imatge.jpg",
            content="Contingut del post",
            slug="post-de-prova",
            author=self.author,
        )
        post.tags.add(self.tag)  # Afegim l'etiqueta al post
        # Comprovem que el mètode __str__ del post retorna el títol correctament
        self.assertEqual(str(post), "Post de prova")

# Tests per verificar el comportament de les vistes del blog
class BlogViewsTest(TestCase):
    def setUp(self):
        # Configurem un autor, una etiqueta i un post de prova per fer els tests
        self.author = Author.objects.create(nom="Nom", cognom="Cognom", email_address="test@example.com")
        self.tag = Tag.objects.create(caption="Etiqueta", slug="etiqueta")
        self.post = Post.objects.create(
            title="Títol",
            excerpt="Resum",
            img_name="imatge.jpg",
            slug="titol",
            content="Contingut llarg del post",
            author=self.author
        )
        # Afegim l’etiqueta al post
        self.post.tags.add(self.tag)

    def test_starting_page_view(self):
        # Comprovem que la vista de la pàgina inicial es carrega correctament (codi 200)
        response = self.client.get(reverse("starting-page"))
        self.assertEqual(response.status_code, 200)
        # Comprovem que s'utilitza la plantilla correcta
        self.assertTemplateUsed(response, "blog/index.html")

    def test_posts_view(self):
        # Comprovem que la vista de tots els posts retorna correctament
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/posts.html")

    def test_post_detail_view(self):
        # Comprovem que la vista de detall d’un post concret funciona
        response = self.client.get(reverse("post-detail", args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post-detail-page.html")

    def test_autors_view(self):
        # Comprovem que la vista de llistat d’autors retorna correctament
        response = self.client.get("/autors/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/autors.html")

    def test_author_detail_view(self):
        # Comprovem que la vista de detall d’un autor funciona
        response = self.client.get(reverse("author-detail", args=[self.author.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/author-detail-page.html")

    def test_tags_view(self):
        # Comprovem que la vista de llistat d’etiquetes funciona
        response = self.client.get("/tags/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/tags.html")

    def test_tag_detail_view(self):
        # Comprovem que la vista de detall d’una etiqueta concreta retorna correctament
        response = self.client.get(reverse("tag-detail", args=[self.tag.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/tag-detail-page.html")
