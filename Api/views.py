from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from . models import Post
from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def EndpointView(request):
    endpionts = 'post/,  post/<str:pk>/'
    return Response(endpionts)


@api_view(['GET', 'POST'])
def Bloglistview(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def BlogDetailview(request, id):
    post = get_object_or_404(Post, pk=id)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response({"message": "Post deleted successfully"}, status=status.HTTP_204_NO_CONTENT)