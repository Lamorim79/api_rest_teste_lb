from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Cliente
from .models import ClienteProduto
from .serializers import ClienteSerializer
from .serializers import ClienteProdutoSerializer
import json
import requests

# Create your views here.


class ClientesView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request,id=0):
        if (id>0):
            clientes=list(Cliente.objects.filter(id=id).values())
            if len(clientes) > 0:
                cliente=clientes[0]
                dados = {'message': "Successo", 'cliente': cliente}
            else:
                dados = {'message': "cliente não encontrado..."} 
            return JsonResponse(dados)       
        else:    
            clientes = list(Cliente.objects.values())
            if len(clientes) > 0:
                dados = {'message': "Successo", 'Clientes': clientes}
            else:
                dados = {'message': "Clientes não encontrados..."}
            return JsonResponse(dados)        
    
    def post(self,request):
        jd = json.loads(request.body)
        email = Cliente.objects.filter(email=jd['email'])
        if not email:
            Cliente.objects.create(nome=jd['nome'],email=jd['email'])
            dados = {'message': "Successo"}
        else: dados = {'message': "Email já cadastrado"}     
        return JsonResponse(dados)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        clientes=list(Cliente.objects.filter(id=id))
        if len(clientes) > 0:
            cliente=clientes[0]        
            cliente.nome=jd['nome']
            cliente.save()
            dados = {'message': "Successo"} 
        else:
            dados = {'message': "Cliente não encontrado..."}
        return JsonResponse(dados)         
    
    def delete(self,request,id):
         clientes=list(Cliente.objects.filter(id=id))
         if len(clientes) > 0:
             Cliente.objects.filter(id=id).delete()
             ClienteProduto.objects.filter(id_cliente=id).delete()
             dados = {'message': "Excluído com successo"}
         else:
             dados = {'message': "Cliente não encontrado..."}
         return JsonResponse(dados)         
  

class ClienteProdutosView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request,id):
       
        clienteProdutos = list(ClienteProduto.objects.filter(id_cliente=id).values())
        if len(clienteProdutos) > 0:
            resposta_final={
                'cliente': clienteProdutos[0]['id_cliente'],
                'produtos_favoritos':[]
            }
            
            for produto in clienteProdutos:                
                url_api = 'http://challenge-api.luizalabs.com/api/product/'+produto['id_produto']+'/'
                print(url_api)
                try:
                    response = requests.get(url_api)                    
                    if response.status_code == 200:
                        dados = response.json()                             
                        resposta_final['produtos_favoritos'].append(dados)                    
                except Exception as e:
                    return JsonResponse({'error': str(e)}, status=500)
            dados = {'message': "Successo",'clienteProdutos':resposta_final}
        else:
             dados = {'message': "Produto não encontrado..."}
        return JsonResponse(dados)
            
    def post(self,request):
        jd = json.loads(request.body)
        produto_favorito = ClienteProduto.objects.filter(id_cliente=jd['id_cliente'],id_produto=jd['id_produto'])
        if not produto_favorito:
            url_api = 'http://challenge-api.luizalabs.com/api/product/'+jd['id_produto']+'/'            
            try:             
                response = requests.get(url_api)
                if response.status_code == 200:
                    print(response)
                    ClienteProduto.objects.create(id_cliente=jd['id_cliente'],id_produto=jd['id_produto'])
                    dados = {'message': "Successo"}
                else:
                    dados = {'message': "Esse produto Não existe"}                   
            except Exception as e:                
                return JsonResponse({'error': str(e)}, status=500)       
        else: dados = {'message': "Produto já favoritado"}         
        return JsonResponse(dados)
    
    