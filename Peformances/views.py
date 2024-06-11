from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from.models import UserPeformance, Event
from .serializer import UserPeformanceSerializer, UserPeformanceDetailSerializer, UserEventSerializer
from django.http import Http404
from triathlon_nexus.permissions import IsOwnerOrReadOnly

class UserPeformanceListView(generics.ListCreateAPIView):
    serializer_class = UserPeformanceSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = UserPeformance.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserPeformanceDetailListView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserPeformanceDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = UserPeformance.objects.all()

class UserEventListView(generics.ListCreateAPIView):
    serializer_class = UserEventSerializer
    queryset = Event.objects.all()

class UserEventListDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserEventSerializer
    queryset = Event.objects.all()