from rest_framework import serializers
from .models import Border

class BorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Border
        fields = ('__all__')

