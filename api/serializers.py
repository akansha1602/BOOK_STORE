from book_outlet.models import Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        #fields=('title','rating')
        fields='__all__'
 
