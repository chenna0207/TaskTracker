from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.contrib.auth.models import User
from .models import Project, UserProjectRole, Task
from .serializers import ProjectSerializer, UserProjectRoleSerializer, TaskSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

@api_view(['GET', 'POST'])
def find_users(request):
    users = User.objects.filter(username=request.data.get('username', ''))
    if users.exists():
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    else:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    # Create the user object
    try:
        user = User.objects.create(username=username, password=make_password(password))
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserProjectRoleViewSet(viewsets.ModelViewSet):
    queryset = UserProjectRole.objects.all()
    serializer_class = UserProjectRoleSerializer
