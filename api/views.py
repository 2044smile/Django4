from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ViewSet

from api.models import Item
from .serializers import ItemSerializer


@api_view(['GET'])
def get_data(request):
    """
    :param request:
    :return: items list
    """
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_item(request):
    """
    :param request:
    :return: create item
    """
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
