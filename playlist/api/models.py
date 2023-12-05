from django.db import models
import string
import random

def randomCodeGenerator():
    lengthOfCode = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase), k = lengthOfCode)
        if Group.objects.filter(code=code).count == 0:
            break
    return code
        

# Create your models here.
class Group(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50,unique=True)
    guest_can_pause = models.BooleanField(null=False,default=False)
    votesToSkip = models.IntegerField(null=False,default=1)
    createdAt = models.DateTimeField(auto_now_add=True)