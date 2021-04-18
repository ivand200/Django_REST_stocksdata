from rest_framework.serializers import ModelSerializer
from .models import SP500, DJ30, Div, Index

class SP500Serializer(ModelSerializer):
    class Meta:
        model = SP500
        fields = ["symbol", "name", "momentum_12_2", "p_e", "e_p"]


class DJ30Serializer(ModelSerializer):
    class Meta:
        model = DJ30
        fields = ["symbol", "name", "momentum_12_2", "p_e", "e_p", "p_div"]

class DivSerializer(ModelSerializer):
    class Meta:
        model = Div
        fields = ["symbol", "name", "p_div"]

class IndexSerializer(ModelSerializer):
    class Meta:
        model = Index
        fields = ["symbol", "name", "momentum", "ma10"]
