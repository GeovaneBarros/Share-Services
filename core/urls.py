from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'contato', ContatoViewSet)
router.register(r'endereco', EnderecoViewSet)
router.register(r'empresa', EmpresaViewSet)
router.register(r'descricao', DescricaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]