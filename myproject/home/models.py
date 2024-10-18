from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_TYPE_CHOICES = (
        ('regular', 'Regular'),
        ('premium', 'Premium'),
        ('wholesale', 'Wholesale'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='regular')

    def __str__(self):
        return f"{self.user.username} Profile"
