from django.db import models

# Create your models here.

class Cliente(models.Model):
    id=models.AutoField(primary_key=True)
    nome=models.CharField(max_length=150)
    email=models.EmailField(max_length=254)
    
    
class ClienteProduto(models.Model):
    id=models.AutoField(primary_key=True)
    id_cliente=models.CharField(max_length=50)
    id_produto=models.CharField(max_length=200)    