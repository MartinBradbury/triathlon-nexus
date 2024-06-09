from rest_framework import serializers
from .models import Like
from django.db import IntegrityError

class LikesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')


    """
    Handle duplicate Likes
    """
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'Possible Duplication'
            })

    class Meta:
        model = Like
        fields = [
            'id', 'owner', 'created_at', 'post',
        ]