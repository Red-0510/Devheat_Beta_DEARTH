from django.db import models
from tinymce.models import HTMLField

class Event(models.Model):
    serial_no=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    slug=models.CharField(max_length=100)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    description=models.CharField(max_length=150)
    content=HTMLField()
    pub_timestamp=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to="event/images")

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.serial_no)
        super().delete()



