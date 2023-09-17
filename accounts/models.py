from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_premium_user = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
