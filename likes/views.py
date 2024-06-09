from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from.models import Like
from .serializer import LikesSerializer
from django.http import Http404
from triathlon_nexus.permissions import IsOwnerOrReadOnly

class LikeList(generics.ListCreateAPIView):
    serializer_class = LikesSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class LikeDetail(generics.RetrieveDestroyAPIView):
    serializer_class = LikesSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Like.objects.all()