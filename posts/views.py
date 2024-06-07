from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from.models import Posts
from .serializer import PostSerializer
from django.http import Http404
from triathlon_nexus.permissions import IsOwnerOrReadOnly

class PostList(APIView):
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        posts = Posts.objects.all() 
        serializer = PostSerializer(
            posts, many=True, context={'request': request}
        )
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PostSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


