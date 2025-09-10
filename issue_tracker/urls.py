from django.urls import path, include
from rest_framework import routers
from .views import OrganizationViewSet, UserViewSet, ProjectViewSet, IssueViewSet

router = routers.DefaultRouter()
router.register(r'organizations', OrganizationViewSet)
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'issues', IssueViewSet)

from .views import RegisterView

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
]
