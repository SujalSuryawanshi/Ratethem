from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
class Human(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    name = models.CharField(max_length=100)
    bio = models.TextField()
    occupation = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class RatingCount(models.Model):
    human = models.OneToOneField(Human, on_delete=models.CASCADE, related_name="rating_count")
    excellent = models.PositiveIntegerField(default=0)
    good = models.PositiveIntegerField(default=0)
    okay = models.PositiveIntegerField(default=0)
    bad = models.PositiveIntegerField(default=0)
    pathetic = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Ratings for {self.human.name}"
