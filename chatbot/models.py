from django.db import models

# Create your models here.
class ChatMessage(models.Model):
    user = models.CharField(max_length=100)
    message = models.TextField()
    bot_response = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}: {self.message[:50]}"