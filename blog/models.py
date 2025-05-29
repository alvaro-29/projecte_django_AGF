from django.db import models
from django.utils import timezone

# Create your models here.

class Author(models.Model):
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    email_address = models.EmailField()
    
    def __str__(self):
        return f"{self.nom} {self.cognom}"

class Tag(models.Model):
    caption = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.caption
   
class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    img_name = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    
    # One-to-Many relationship with Author
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="posts",null=True)
    
    # Many-to-Many relationship with Tag
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.title