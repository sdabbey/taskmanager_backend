from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=500)
    content = models.TextField(null=True)
    pub_date = models.DateField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']
