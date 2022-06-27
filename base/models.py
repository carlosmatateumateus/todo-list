from django.db import models

class WriteDown(models.Model):

    title = models.CharField(max_length=60)
    finish=models.BooleanField()
    body = models.TextField()
    
    created = models.DateTimeField(auto_now=True)
    update = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title