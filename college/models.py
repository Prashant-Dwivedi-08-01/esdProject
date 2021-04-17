from django.db import models

# Create your models here.
class Councelling(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)
    course =  models.CharField(max_length = 100)
    query =  models.CharField(max_length = 500)
    session_date =  models.CharField(max_length = 100)
    session_time =  models.CharField(max_length = 100)
    

    def __str__(self):
        return self.name