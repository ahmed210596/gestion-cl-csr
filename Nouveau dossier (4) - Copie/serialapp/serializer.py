from authapp.serializer import UserSerializer
from rest_framework import serializers

from serialapp.models import Serial


class SerialSerializer(serializers.ModelSerializer):
    creator = UserSerializer()
    editor = UserSerializer()

    class Meta:
        model = Serial
        fields = ('id', 'serial_number','creator','editor','created_at', 'updated_at')