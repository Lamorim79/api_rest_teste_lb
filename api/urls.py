from django.urls import path
from .views import ClientesView
from .views import ClienteProdutosView

urlpatterns=[
    path('clientes',ClientesView.as_view(),name='Clientes_list'),
    path('clientes/<int:id>',ClientesView.as_view(),name='clientes_process'),
    path('clientes/<int:id>/produtos',ClienteProdutosView.as_view(),name='clienteProdutos_list'),
    path('clientes/produtos',ClienteProdutosView.as_view(),name='clienteProdutos_list'),
]


