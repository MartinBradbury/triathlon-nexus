from rest_framework.response import Response
from rest_framework import status, permissions, generics
from.models import Comment
from .serializer import CommentSerializer, CommentDetailSerializer
from django.http import Http404
from triathlon_nexus.permissions import IsOwnerOrReadOnly

class CommentList(generics.ListCreateAPIView):
    """
    Create a comment or List comments
    """
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()