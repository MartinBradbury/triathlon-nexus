from rest_framework import serializers
from .models import UserPeformance, Event
from django.db import IntegrityError

class UserEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description',]

class UserPeformanceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    title = serializers.ReadOnlyField(source='event.title')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = UserPeformance
        fields = ['id', 'owner', 'event', 'time_field', 'complete','is_owner', 'title', 'content',]

class UserPeformanceDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    event = serializers.ReadOnlyField(source='event.title')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = UserPeformance
        fields = ['id', 'owner', 'event', 'time_field', 'complete','is_owner', 'content',]
