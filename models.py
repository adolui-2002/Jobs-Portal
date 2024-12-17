from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

# User profile


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    def __str__(self):
        return self.user.username


# Job posting

from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=100)
    company = models.CharField(max_length=100, default="Unknown Company")
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')  # Link to User

    def __str__(self):
        return self.title




# Job application
class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    candidate = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    cover_letter = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidate.username} - {self.job.title}"

