from rest_framework.response import Response
from rest_framework.decorators import api_view
from models import Author
from serializers import AuthorSerializer


@api_view(['GET'])
def author(request):
    author = Author.objects.all()[:5]
    serializer = AuthorSerializer(author, many=True)
    return Response(serializer.data)