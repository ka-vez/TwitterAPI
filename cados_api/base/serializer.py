from rest_framework import serializers
from .models import Advocate

#create your serializrs here
class AdvocateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advocate
        fields = '__all__'
