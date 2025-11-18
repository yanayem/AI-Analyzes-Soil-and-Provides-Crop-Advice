from django.db import models
from django.contrib.auth.models import User

# -------------------------
# Helper function for file uploads
# -------------------------
def user_directory_path(instance, filename):
    return f'user_{instance.user.id}/{filename}'


# -------------------------
# UserProfile model
# -------------------------
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to=user_directory_path,
        blank=True,
        null=True,
        default='profile_pics/default.png'
    )
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True, default="Soil Analyst")
    last_email_change = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"
