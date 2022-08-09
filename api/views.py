from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema

from api.models import Item
from .serializers import ItemSerializer


@swagger_auto_schema(
    method='GET',
    tags=['FBV items'],
    responses={200: 'Success'}
)
@api_view(['GET'])
def get_item(request):
    """
    :param request:
    :return: items list

    직렬화 쿼리셋, 모델 인스턴스 등의 복잡한 데이터를 JSON, XML 타입으로 변환 가능
    """
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method='POST',
    tags=['FBV items'],
    responses={200: 'Success'}
)
@api_view(['POST'])
def add_item(request):
    """
    :param request:
    :return: create item

    Deserializer 받은 데이터(POST) validating
    반드시 is_valid() 사용
    """
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
