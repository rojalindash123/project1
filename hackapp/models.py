from django.db import models

# Create your models here.
class Signin(models.Model):
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name="Signins"

