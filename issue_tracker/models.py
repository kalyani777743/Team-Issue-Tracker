
from django.contrib.auth.models import AbstractUser
from django.db import models

class Organization(models.Model):
	name = models.CharField(max_length=255)
	owner = models.ForeignKey('User', related_name='owned_organizations', on_delete=models.CASCADE)

class User(AbstractUser):
	organization = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.SET_NULL)
	ROLE_CHOICES = (
		('owner', 'Owner'),
		('manager', 'Manager'),
		('member', 'Member'),
	)
	role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member')

class Project(models.Model):
	name = models.CharField(max_length=255)
	organization = models.ForeignKey(Organization, related_name='projects', on_delete=models.CASCADE)

class Issue(models.Model):
	STATUS_CHOICES = (
		('open', 'Open'),
		('in_progress', 'In Progress'),
		('closed', 'Closed'),
	)
	PRIORITY_CHOICES = (
		('low', 'Low'),
		('medium', 'Medium'),
		('high', 'High'),
	)
	title = models.CharField(max_length=255)
	description = models.TextField()
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
	priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
	due_date = models.DateField(null=True, blank=True)
	assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
	project = models.ForeignKey(Project, related_name='issues', on_delete=models.CASCADE)
	attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
