from rest_framework import serializers
from .models import ProfileModel

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = '__all__'
