from rest_framework.response import Response
from rest_framework.decorators import api_view
from models import Book
from serializers import BookSerializer


@api_view(['GET'])
def book(request):
    book = Book.objects.all()[:5]
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)