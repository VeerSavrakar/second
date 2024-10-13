from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
class MyModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.TextField()

    def __str__(self):
        return f"MyModel: {self.field1}"
    
@receiver(post_save ,sender=MyModel)
def _post_save_receiver(sender,instance, **kwargs):
    print("Signal recived",instance)
    
