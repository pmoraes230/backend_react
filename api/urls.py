# api/urls.py
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'api', views.ItemListCreate, 'api')

urlpatterns = [
    path('', include(router.urls)),
]