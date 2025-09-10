from rest_framework import serializers
from .models import Organization, User, Project, Issue

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name', 'owner']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'organization']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'organization']

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = [
            'id', 'title', 'description', 'status', 'priority', 'due_date',
            'assigned_to', 'project', 'attachment', 'created_at', 'updated_at'
        ]
