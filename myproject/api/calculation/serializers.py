from rest_framework import serializers

class FreightCalculationSerializer(serializers.Serializer):
    country_id = serializers.IntegerField()
    category_title = serializers.CharField()
    destination_id = serializers.CharField()
    weight = serializers.DecimalField(max_digits=10, decimal_places=2)
