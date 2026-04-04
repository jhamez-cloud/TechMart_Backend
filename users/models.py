'''Documentation String'''
from django.db import models

class UserProfile(models.Model):
    '''Documentation String'''
    firebase_uid = models.CharField(max_length=255, unique=True)

    profile_pic = models.ImageField(upload_to="profiles/",null=True,blank=True)
    user_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Edit: {self.user_name}"
