from django.db import models

def upload_to(instance, filename):
    return '{filename}'.format(filename=filename)

class Chat(models.Model):
    username = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    img = models.FileField(upload_to=upload_to, null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)