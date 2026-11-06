
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APITestCase

from .models import Categoria, Produto
from .serializers import CategoriaSerializer, ProdutoSerializer


class CategoriaSerializerTests(TestCase):

    def test_categoria_com_nome_vazio(self):

        serializer = CategoriaSerializer(data={
            'nome': '   ',
            'descricao': ''
        })

        self.assertFalse(serializer.is_valid())

    def test_categoria_remove_espacos_do_nome(self):

        serializer = CategoriaSerializer(data={
            'nome': '  Lanches  ',
            'descricao': ''
        })

        self.assertTrue(serializer.is_valid())
        self.assertEqual(
            serializer.validated_data['nome'],
            'Lanches'
        )


class ProdutoSerializerTests(TestCase):

    def setUp(self):

        self.categoria = Categoria.objects.create(
            nome='Lanches',
            descricao='Categoria de lanches'
        )

    def test_produto_com_nome_vazio(self):

        serializer = ProdutoSerializer(data={
            'nome': '   ',
            'preco': '10.00',
            'disponivel': True,
            'categoria': self.categoria.id
        })

        self.assertFalse(serializer.is_valid())

    def test_produto_com_preco_negativo(self):

        serializer = ProdutoSerializer(data={
            'nome': 'Hamburguer',
            'preco': '-10.00',
            'disponivel': True,
            'categoria': self.categoria.id
        })

        self.assertFalse(serializer.is_valid())

    def test_produto_com_dados_validos(self):

        serializer = ProdutoSerializer(data={
            'nome': 'Hamburguer',
            'preco': '15.00',
            'disponivel': True,
            'categoria': self.categoria.id
        })

        self.assertTrue(serializer.is_valid())

    def test_produto_disponivel_por_padrao(self):

        produto = Produto.objects.create(
            nome='Suco',
            preco='7.00',
            categoria=self.categoria
        )

        self.assertTrue(produto.disponivel)


class ProdutoAPITests(APITestCase):

    def setUp(self):

        User = get_user_model()

        self.usuario = User.objects.create_user(
            username='teste',
            password='senha123'
        )

        self.client.force_authenticate(user=self.usuario)

        self.categoria = Categoria.objects.create(
            nome='Bebidas',
            descricao='Bebidas da lanchonete'
        )

        Produto.objects.create(
            nome='Suco',
            preco='7.00',
            disponivel=True,
            categoria=self.categoria
        )

        Produto.objects.create(
            nome='Refrigerante',
            preco='6.00',
            disponivel=False,
            categoria=self.categoria
        )

    def test_filtro_produtos_indisponiveis(self):

        url = reverse('produto-list')

        resposta = self.client.get(
            url,
            {'disponivel': 'false'}
        )

        self.assertEqual(resposta.status_code, 200)

        produtos = resposta.data['results']

        self.assertEqual(len(produtos), 1)

        self.assertEqual(
            produtos[0]['nome'],
            'Refrigerante'
        )

