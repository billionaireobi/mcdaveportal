from django.db import models
from django.contrib.auth.models import User
import uuid


# create events
class passwordreset(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    reset_id=models.UUIDField(default=uuid.uuid4, unique=True,editable=False)
    created_when=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"password reset for{self.user.username} at {self.created_when}"
    


    
class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title