from django.http import response
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from api.serilizers import ProjectSerializer
from authapi.models import Project

@api_view(['GET'])
def getRoute(request):
    routes =[
        
        {'GET' : 'api/projects'},
        {'POST': 'api/user/token'}
    ]
    
    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProjects(request):
    projects = Project.objects.all()
    serilize = ProjectSerializer(projects, many=True)
    return Response(serilize.data)