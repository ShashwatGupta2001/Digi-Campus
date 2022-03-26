from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class HallStudents(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

class hallPresence(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    user_visiting=models.IntegerField(null=True)
    in_hall=models.BooleanField(default=False)
    laptop=models.BooleanField(default=False)
    timeEntered=models.DateTimeField(null=True)
    timeExit=models.DateTimeField(null=True)