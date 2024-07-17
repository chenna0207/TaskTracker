from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Project, UserProjectRole, Task

class UserProjectRoleSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    project_name = serializers.CharField(source='project.name', read_only=True)

    class Meta:
        model = UserProjectRole
        fields = ['id', 'role', 'user', 'user_name', 'project', 'project_name']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['id', 'username','password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ProjectSerializer(serializers.ModelSerializer):
    assigned_users = UserProjectRoleSerializer(many=True, read_only=True, source='userprojectrole_set')

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'owner', 'assigned_users']

class TaskSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner.username', read_only=True)
    assigned_user_name = serializers.CharField(source='assigned_user.username', read_only=True)
    project_name = serializers.CharField(source='project.name', read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'description', 'due_date', 'status', 'owner', 'owner_name', 'assigned_user', 'assigned_user_name', 'project', 'project_name']
