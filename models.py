from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    total_rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    total_rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    content = models.TextField()
    rating = models.FloatField()
    author = models.ForeignKey(Author, null=True, blank=True)
    book = models.ForeignKey(Book, null=True, blank=True)

    def __str__(self):
        return self.content    