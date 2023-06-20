from django.db import models

# Create your models here.
class Teacher(models.Model):
    name       = models.CharField(max_length=50)
    age        = models.PositiveIntegerField()
    salary     = models.IntegerField()
    experience = models.BooleanField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['id']
