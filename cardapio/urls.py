
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    CategoriaViewSet,
    ProdutoViewSet,
    EstadosIBGEView,
    MunicipiosIBGEView,
)


router = DefaultRouter()

router.register(
    r'categorias',
    CategoriaViewSet,
    basename='categoria'
)

router.register(
    r'produtos',
    ProdutoViewSet,
    basename='produto'
)


urlpatterns = [
    path(
        'ibge/estados/',
        EstadosIBGEView.as_view(),
        name='ibge-estados'
    ),

    path(
        'ibge/estados/<int:uf_id>/municipios/',
        MunicipiosIBGEView.as_view(),
        name='ibge-municipios'
    ),

] + router.urls
