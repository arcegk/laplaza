from rest_framework import serializers
from .models import Plato

class ComboSerializer(serializers.Serializer):
	id = serializers.IntegerField()
	name_combo = serializers.CharField(max_length=30)
	no_lunch = serializers.IntegerField()
	no_lunch_special = serializers.IntegerField()
	normal_price = serializers.FloatField()
	price = serializers.FloatField()


class PlatoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Plato
		fields = ('id','nombre','tipo','precio','precio_extra')