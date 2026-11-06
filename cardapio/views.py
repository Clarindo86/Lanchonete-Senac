
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
import requests

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .services import buscar_estados, buscar_municipios

from .models import Categoria, Produto
from .serializers import CategoriaSerializer, ProdutoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):

    queryset = Categoria.objects.all().order_by('id')
    serializer_class = CategoriaSerializer

    @action(detail=True, methods=['get'])
    def produtos(self, request, pk=None):

        categoria = self.get_object()

        produtos = categoria.produtos.all()

        serializer = ProdutoSerializer(produtos, many=True)

        return Response(serializer.data)


class ProdutoViewSet(viewsets.ModelViewSet):

    serializer_class = ProdutoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nome']

    def get_queryset(self):

        queryset = Produto.objects.select_related('categoria').all().order_by('id')

        # Filtro por disponibilidade
        disponivel = self.request.query_params.get('disponivel')

        if disponivel is not None:

            disponivel = disponivel.strip().lower()

            if disponivel == 'true':
                queryset = queryset.filter(disponivel=True)

            elif disponivel == 'false':
                queryset = queryset.filter(disponivel=False)

        # Filtro por categoria
        categoria_id = self.request.query_params.get('categoria')

        if categoria_id:
            queryset = queryset.filter(categoria_id=categoria_id)

        return queryset


    
class EstadosIBGEView(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        try:
            estados = buscar_estados()
            return Response(estados)

        except requests.RequestException:
            return Response(
                {"erro": "Não foi possível consultar os estados no IBGE."},
                status=503
            )


class MunicipiosIBGEView(APIView):

    permission_classes = [AllowAny]

    def get(self, request, uf_id):
        try:
            municipios = buscar_municipios(uf_id)
            return Response(municipios)

        except requests.RequestException:
            return Response(
                {"erro": "Não foi possível consultar os municípios no IBGE."},
                status=503
            )

