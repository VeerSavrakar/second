from django.db import models
from django.db.models import signals
from django.db.models.signals import post_save,pre_save
# Create your models here.\
from django.dispatch import receiver
import threading

class Author(models.Model):
    name=models.CharField(max_length=100)
    
    

@receiver(post_save, sender=Author)
def _post_save_receiver(sender,instance, **kwargs):
    print(f"Signal received in thread: {threading.current_thread().name}")