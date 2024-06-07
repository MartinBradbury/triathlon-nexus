from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.first_name')

    class Meta:
        model = Profile
        fields = ['id', 'owner', 'created_at', 'updated_at', 'first_name', 'last_name',
                  'email', 'date_of_birth', 'gender', 'fitness_level', 'image', 'content',]
            