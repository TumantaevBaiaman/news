from rest_framework import serializers
from .models import We


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = We
        fields = [
            'id', 'user', 'option', 'grate', 'content'
        ]
        read_only_fields = ['user']