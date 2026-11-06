
from rest_framework import serializers
from .models import Categoria, Produto


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'descricao']

    def validate_nome(self, value):
        nome = value.strip()

        if not nome:
            raise serializers.ValidationError(
                "O nome da categoria não pode ficar vazio."
            )

        return nome


class ProdutoSerializer(serializers.ModelSerializer):

    categoria_nome = serializers.CharField(
        source='categoria.nome',
        read_only=True
    )

    class Meta:
        model = Produto
        fields = [
            'id',
            'nome',
            'preco',
            'disponivel',
            'categoria',
            'categoria_nome'
        ]

    def validate_nome(self, value):
        nome = value.strip()

        if not nome:
            raise serializers.ValidationError(
                "O nome do produto não pode ficar vazio."
            )

        return nome

    def validate_preco(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "O preço não pode ser negativo."
            )

        return value
