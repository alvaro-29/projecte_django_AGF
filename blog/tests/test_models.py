from django.test import TestCase
from blog.models import Author, Tag, Post
from django.utils import timezone

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