from rest_framework import serializers
from .models import Type

class TypeSerializer(serializers.ModelSerializer):
    class meta:
        model = Type
        fields = "__all__"
