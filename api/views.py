from rest_framework.response import Response
from rest_framework.decorators import api_view
from book_outlet.models import Book
from .serializers import BookSerializer


@api_view(['GET'])
def getData(request):
    #person={'name':'Dennis','age':28}
    book = Book.objects.all()[:5]
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)