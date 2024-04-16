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
                datos = {'message': "Successo", 'cliente': cliente}
            else:
                datos = {'message': "cliente não encontrado..."} 
            return JsonResponse(datos)       
        else:    
            clientes = list(Cliente.objects.values())
            if len(clientes) > 0:
                datos = {'message': "Successo", 'Clientes': clientes}
            else:
                datos = {'message': "clientes não encontrados..."}
            return JsonResponse(datos)        
    
    def post(self,request):
        jd = json.loads(request.body)
        email = Cliente.objects.filter(email=jd['email'])
        if not email:
            Cliente.objects.create(nome=jd['nome'],email=jd['email'])
            datos = {'message': "Successo"}
        else: datos = {'message': "Email já cadastrado"}  
               
        
        return JsonResponse(datos)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        clientes=list(Cliente.objects.filter(id=id))
        if len(clientes) > 0:
            cliente=clientes[0]        
            cliente.nome=jd['nome']
            cliente.save()
            datos = {'message': "Successo"} 
        else:
            datos = {'message': "Cliente não encontrado..."}
        return JsonResponse(datos)         
    
    def delete(self,request,id):
         clientes=list(Cliente.objects.filter(id=id))
         if len(clientes) > 0:
             Cliente.objects.filter(id=id).delete()
             ClienteProduto.objects.filter(id_cliente=id).delete()
             datos = {'message': "Excluído com successo"}
         else:
             datos = {'message': "Cliente não encontrado..."}
         return JsonResponse(datos)         
  

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
                    # Fazendo a requisição GET
                    response = requests.get(url_api)

                    # Verifica se a requisição foi bem-sucedida (código 200)
                    if response.status_code == 200:
                        # Convertendo a resposta para JSON
                        data = response.json()
                        # Retornando os dados como resposta da sua API
                        print(data)
                        
                        resposta_final['produtos_favoritos'].append(data)
                    
                except Exception as e:
                    # Se ocorrer algum erro na requisição, retorna um erro
                    return JsonResponse({'error': str(e)}, status=500)
            datos = {'message': "Successo",'clienteProdutos':resposta_final}
        else:
             datos = {'message': "Produto não encontrado..."}
        return JsonResponse(datos)
            
    def post(self,request):
        jd = json.loads(request.body)
        produto_favorito = ClienteProduto.objects.filter(id_cliente=jd['id_cliente'],id_produto=jd['id_produto'])
        if not produto_favorito:
            url_api = 'http://challenge-api.luizalabs.com/api/product/'+jd['id_produto']+'/'
            print(url_api)
            try:
                # Fazendo a requisição GET
                response = requests.get(url_api)

                # Verifica se a requisição foi bem-sucedida (código 200)
                if response.status_code == 200:
                    print(response)
                    ClienteProduto.objects.create(id_cliente=jd['id_cliente'],id_produto=jd['id_produto'])
                    datos = {'message': "Successo"}
                else:
                    datos = {'message': "Esse produto Não existe"}                   
            except Exception as e:
                # Se ocorrer algum erro na requisição, retorna um erro
                return JsonResponse({'error': str(e)}, status=500)
            
            
        else: datos = {'message': "Produto já favoritado"}
           
         
        return JsonResponse(datos)
    
    