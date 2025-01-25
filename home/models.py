
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models

# Custom User Model
class User(AbstractUser):
     groups = models.ManyToManyField(
        Group,
        related_name="home_user_set",  # Custom related name
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
     user_permissions = models.ManyToManyField(
        Permission,
        related_name="home_user_set_permissions",  # Custom related name
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
# Startup Model
class Startup(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    slides = models.FileField(upload_to='slides/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], default='pending')
    pitching_room_empty = models.BooleanField(default=True)  # Determines room status

    def __str__(self):
        return self.name

# Request Model
class PitchRequest(models.Model):
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
    coordinator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Request for {self.startup.name} by {self.coordinator.username}"