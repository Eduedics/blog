from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def Bloglistview(request):
    return Response('hey there')



@api_view(['GET'])
def BlogDetailview(request,id):
    
    return Response('hey there',pk = id)