from rest_framework import serializers
from .models import Author, Book, Review

class AuthorSerializer(serializers.ModelSerializer):
    num_books = serializers.SerializerMethodField()

    def get_num_books(self, author):
        return author.books.count()

    class Meta:
        model = Author
        fields = ['id', 'name', 'total_rating', 'num_books']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
