from rest_framework import serializers
from api.models import Item


class ItemSerializer(serializers.ModelSerializer):
    """
    Serializer(instance)
    Serializer.data
    **데이터베이스에 있는 데이터를 가져와 화면에 출력하는 Serializer

    Create a new instance
    Deserializer(data=)
    .is_valid(raise_exception=True)
    .errors {'email': ['Enter a valid e-mail address.'], 'created': ['This field is required.']}
    .validated_data
    **외부에서 받은 JSON,XML 데이터를 Deserializer 하여 데이터베이스 저장 하는 Deserializer
    """
    class Meta:
        model = Item
        fields = '__all__'

    def create(self, validated_data):
        name = validated_data.pop('name')

        rename = name + " Item"

        item = Item.objects.create(name=rename)

        return item
