
from rest_framework import serializers

from .models import Festival



class FestivalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Festival

        fields = ['id', 'name', 'location', 'capacity', 'start_date', 'end_date']
