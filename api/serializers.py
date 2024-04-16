from rest_framework import serializers

from .models import Cliente
from .models import ClienteProduto


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__' 
        
        
class ClienteProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteProduto
        fields = '__all__'         