from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["transaction_type", "date", "amount", "cpf", "card", "owner", "store_name"]

class UploadSerializer(serializers.Serializer):
    uploaded_file = serializers.FileField()

    class Meta:
        fields = ["uploaded_file"]