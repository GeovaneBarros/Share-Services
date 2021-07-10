from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, PrestadorViewSet, ContatoViewSet, EnderecoViewSet, ClienteViewSet, AvaliacaoViewSet

router = routers.DefaultRouter()
router.register(r'prestador', PrestadorViewSet)
router.register(r'user', UserViewSet)
router.register(r'contato', ContatoViewSet)
router.register(r'endereco', EnderecoViewSet)
router.register(r'cliente', ClienteViewSet)
router.register(r'avaliacao', AvaliacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]