from rest_framework import serializers
from .models import Posts

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size is too large, 2MB maximum.'
            )
        if value.image.width > 4096:
            raise serializer.ValidationError(
                'Image width is too large, 4096px maximum'
            )
        if value.image.height > 4096:
            raise serializer.ValidationError(
                'Image height is too large, 4096 maximum'
            )
        return value

    class Meta:
        model = Posts
        fields = ['id', 'owner', 'created_at', 'updated_at', 'title', 'content',
                  'image', 'is_owner',]
            