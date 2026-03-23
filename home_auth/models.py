from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings


class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    is_authorized = models.BooleanField(default=False)
    login_token = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return self.username


class PasswordResetRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    email = models.EmailField()
    token = models.CharField(max_length=32, default=get_random_string, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    TOKEN_VALIDITY_PERIOD = timezone.timedelta(hours=1)

    def is_valid(self):
        return timezone.now() <= self.created_at + self.TOKEN_VALIDITY_PERIOD

    def send_reset_email(self):
        reset_link = f"http://127.0.0.1:8000/authentication/reset-password/{self.token}/"
        send_mail(
            "Password Reset Request",
            f"Click the following link to reset your password: {reset_link}",
            settings.DEFAULT_FROM_EMAIL,
            [self.email],
            fail_silently=False,
        )