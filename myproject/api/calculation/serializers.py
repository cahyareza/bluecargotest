from rest_framework import serializers

class FreightCalculationSerializer(serializers.Serializer):
    country_id = serializers.CharField()
    category_id = serializers.CharField()
    destination_id = serializers.CharField()
    weight = serializers.IntegerField()
