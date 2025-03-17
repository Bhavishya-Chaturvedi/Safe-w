# voice/models.py
from django.db import models

class VoiceCommand(models.Model):
    command_text = models.TextField() 
    timestamp = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.command_text
