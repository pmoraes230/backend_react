
Backend - Aplicativo de Tarefas

Este é o backend do aplicativo de gerenciamento de tarefas, construído com Django e Django REST Framework. Ele fornece uma API RESTful para operações CRUD (Create, Read, Update, Delete) de tarefas, integrada com um front-end React. O backend gerencia uma entidade Todo com os campos id, name e description.
Tecnologias Utilizadas

Django: Framework web para desenvolvimento rápido e seguro.
Django REST Framework: Biblioteca para criar APIs RESTful.
django-cors-headers: Middleware para habilitar CORS, permitindo comunicação com o front-end React.
SQLite: Banco de dados padrão (pode ser substituído por PostgreSQL ou outro).
Estrutura do Projeto

backend/
├── api/                    # Aplicativo Django para a API
│   ├── migrations/         # Migrações do banco de dados
│   ├── __init__.py
│   ├── admin.py            # Configurações do admin do Django
│   ├── apps.py
│   ├── models.py           # Modelo Todo
│   ├── serializers.py      # Serializadores para a API
│   ├── tests.py
│   ├── urls.py             # Rotas da API
│   ├── views.py            # ViewSets para a API
├── backend/                # Configurações do projeto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py         # Configurações do projeto
│   ├── urls.py             # Rotas principais
│   ├── wsgi.py
├── manage.py               # Script de gerenciamento do Django
├── requirements.txt        # Dependências Python

Pré-requisitos

Python: Versão 3.8 ou superior.
pip: Gerenciador de pacotes Python.
Ambiente virtual (recomendado): venv ou virtualenv.
Front-end React: Configurado em http://localhost:3000 (consulte o repositório do front-end).

Configuração
Siga estas etapas para configurar o backend localmente:

Clone o Repositório (se aplicável):
git clone <URL_DO_REPOSITORIO>
cd backend


Crie e Ative um Ambiente Virtual:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Instale as Dependências: Crie ou atualize o arquivo requirements.txt com:
Django==4.2.13
djangorestframework==3.15.1
django-cors-headers==4.3.1

Instale as dependências:
pip install -r requirements.txt


Aplique as Migrações: Configure o banco de dados SQLite:
python manage.py makemigrations
python manage.py migrate


Crie um Superusuário (Opcional): Para acessar o admin do Django (http://localhost:8000/admin):
python manage.py createsuperuser



Executando o Backend

Inicie o Servidor:
python manage.py runserver

O servidor estará disponível em http://localhost:8000.

Endpoints da API:

Listar Tarefas: GET /api/todos/
Criar Tarefa: POST /api/todos/
Detalhes da Tarefa: GET /api/todos/<id>/
Atualizar Tarefa: PUT /api/todos/<id>/
Deletar Tarefa: DELETE /api/todos/<id>/

Exemplo de payload para criar/atualizar:
{
  "name": "Comprar mantimentos",
  "description": "Comprar leite, pão e ovos."
}



Integração com o Front-end
O backend está configurado para se comunicar com o front-end React em http://localhost:3000. Certifique-se de que:

CORS Está Configurado: No backend/settings.py, verifique:
CORS_ALLOWED_ORIGINS = ["http://localhost:3000"]


Proxy no Front-end: No package.json do React, confirme:
"proxy": "http://localhost:8000"


Teste a Integração:

Inicie o backend:
python manage.py runserver


Inicie o front-end React (em outro terminal):
cd ../test_react
npm start


Acesse http://localhost:3000 e teste as operações CRUD.




Resolução de Problemas

Erro AxiosError: Network Error:

Verifique se o servidor Django está rodando (http://localhost:8000/api/todos/).

Confirme a configuração de CORS e proxy.

Teste o endpoint com Postman ou curl:
curl http://localhost:8000/api/todos/




Migrações Falharam:

Delete o arquivo db.sqlite3 e a pasta api/migrations/ (exceto __init__.py).

Reaplique as migrações:
python manage.py makemigrations
python manage.py migrate




Dependências Faltando:

Atualize o requirements.txt e reinstale:
pip install -r requirements.txt





Estrutura da API

Modelo (api/models.py):
from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


Serializador (api/serializers.py):
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'name', 'description']


ViewSet (api/views.py):
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer

class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


URLs (api/urls.py):
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'todo')

urlpatterns = [
    path('', include(router.urls)),
]



Próximos Passos

Autenticação: Adicione djangorestframework-simplejwt para proteger os endpoints.
Testes: Escreva testes unitários em api/tests.py.
Banco de Dados: Considere usar PostgreSQL para produção.
Deploy: Configure o backend em um servidor como Heroku, AWS, ou Railway.

Contribuição

Fork o repositório.
Crie uma branch (git checkout -b feature/nova-funcionalidade).
Faça commit das mudanças (git commit -m "Adiciona nova funcionalidade").
Push para a branch (git push origin feature/nova-funcionalidade).
Abra um Pull Request.

Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para detalhes.
