from django.db import models

# Create your models here.
class SampleModel(models.Model):
    name = models.CharField(max_length=100)
    roll=models.IntegerField(primary_key=True)
    address=models.TextField(default='Dhaka')
    father_name=models.TextField(default='Rahim')

    def __str__(self):
        return self.name