from django.db import models
from django.contrib.auth.models import User

import uuid

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import uuid

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    topic = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, help_text="Date and time when the article was published")
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    twitter_link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.topic or "Untitled Post"