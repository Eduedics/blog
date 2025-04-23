from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer

# Create your views here.
@api_view(['GET'])
def EndpointView(request):
    endpionts = 'post/,  post/<str:pk>/'
    return Response(endpionts)


@api_view(['GET'])
def Bloglistview(request):
    serializer = PostSerializer()
    return Response(serializer.data)



@api_view(['GET'])
def BlogDetailview(request,id):
    
    return Response('hey there',pk = id)