# API Python Django usando MySQL database
API Rest Backend server utilizando Python Django e MySQL database

## Status:

Finalizado

## Características

CRUD

- CREATE criar novo registro de Cliente  <br> http://127.0.0.1:8000/api/clientes   
- CREATE criar uma lista de Produtos Favoritos única para o Cliente <br> http://127.0.0.1:8000/api/clientes/produtos
- READ consultar os Clientes cadastrados <br> http://127.0.0.1:8000/api/clientes
- READ consultar os Produtos Favoritos do Cliente <br> http://127.0.0.1:8000/api/clientes/1/produtos
- UPDATE atualizar os dados do Cliente <br> http://127.0.0.1:8000/api/clientes/1
- DELETE remover o cadastro do Cliente <br> http://127.0.0.1:8000/api/clientes/1

## Pré-requisitos
- Python instalado
- MySQL instalado

## Como rodar a aplicação
1. Fazer o download do projeto a partir de: <br> (Link) https://github.com/Lamorim79/api_rest_teste_lb <br>
2. Criar ambiente virtual <br> `py -m venv venv ` <p>
3. Ativar o ambiente virtual <br>`./venv/Scripts/activate ` <p>
4. Instalar o conector MySQL <br>`pip install mysqlclient` <p>
5. Instalar requisições HTTP <br>`pip install requests` <p>
6. Prepara as tabelas para serem enviadas ao bd <br>`python manage.py makemigrations` <p>
7. Cria as tabelas no bd <br>`python manage.py migrate` <p>
8. Executa a API <br>`python manage.py runserver`


## Autor
- [Luciano Amorim](https://github.com/Lamorim79)
