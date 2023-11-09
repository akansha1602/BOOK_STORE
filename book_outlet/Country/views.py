from rest_framework.response import Response
from rest_framework.decorators import api_view
from models import Country
from serializers import CountrySerializer


@api_view(['GET'])
def author(request):
    country = Country.objects.all()[:5]
    serializer = CountrySerializer(country, many=True)
    return Response(serializer.data)