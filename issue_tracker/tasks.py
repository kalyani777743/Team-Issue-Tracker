from celery import shared_task
from django.utils import timezone
from .models import Issue

@shared_task
def send_overdue_issue_reminders():
    overdue_issues = Issue.objects.filter(status__in=['open', 'in_progress'], due_date__lt=timezone.now().date())
    for issue in overdue_issues:
        # Placeholder: send email or notification to assigned user
        pass
