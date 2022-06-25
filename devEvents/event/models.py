from django.db import models


class Event(models.Model):
    serial_no=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    start_time=models.DateTimeField(auto_now_add=True,blank=True)
    end_time=models.DateTimeField(auto_now_add=True,blank=True)
    description=models.TextField()
    content=models.TextField()
    pub_timestamp=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to="event/images")

    def __str__(self):
        return self.title



