from rest_framework.response import Response
from rest_framework.decorators import api_view
from models import Address
from serializers import AddressSerializer


@api_view(['GET'])
def address(request):
    address = Address.objects.all()[:5]
    serializer = AddressSerializer(address, many=True)
    return Response(serializer.data)