from rest_framework import serializers

class ComboSerializer(serializers.Serializer):
	id = serializers.IntegerField()
	name_combo = serializers.CharField(max_length=30)
	no_lunch = serializers.IntegerField()
	no_lunch_special = serializers.IntegerField()
	normal_price = serializers.FloatField()
	price = serializers.FloatField()