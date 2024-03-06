from django.db import models
from django.contrib.auth.models import User
class Todo(models.Model):
    title=models.CharField(max_length=200)
    content=models.CharField(max_length=500)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.title+":"+self.content

# Create your models here.
