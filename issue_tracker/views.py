
from rest_framework import generics, viewsets, permissions, status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from .models import Organization, User, Project, Issue
from .serializers import OrganizationSerializer, UserSerializer, ProjectSerializer, IssueSerializer

class RegisterView(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [permissions.AllowAny]

	def create(self, request, *args, **kwargs):
		data = request.data.copy()
		if 'password' in data:
			data['password'] = make_password(data['password'])
		# Allow role selection, default to 'member' if not provided
		if 'role' not in data:
			data['role'] = 'member'
		# Only allow 'owner' role if user is admin
		if data.get('role') == 'owner' and not request.user.is_staff:
			return Response({'detail': 'Only admin can register as owner.'}, status=status.HTTP_403_FORBIDDEN)
		serializer = self.get_serializer(data=data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class OrganizationViewSet(viewsets.ModelViewSet):
	queryset = Organization.objects.all()
	serializer_class = OrganizationSerializer
	permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]

class ProjectViewSet(viewsets.ModelViewSet):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer
	permission_classes = [permissions.IsAuthenticated]

class IssueViewSet(viewsets.ModelViewSet):
	queryset = Issue.objects.all()
	serializer_class = IssueSerializer
	permission_classes = [permissions.IsAuthenticated]
	filterset_fields = ['status', 'priority', 'due_date']
