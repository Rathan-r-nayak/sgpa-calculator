from django.db import models

# Create your models here.
class cgpa_db(models.Model):
    usn=models.TextField(max_length=10,null=True)
    sem1=models.FloatField(null=True)
    sem2=models.FloatField(null=True)
    sem3=models.FloatField(null=True)
    sem4=models.FloatField(null=True)
    sem5=models.FloatField(null=True)
    sem6=models.FloatField(null=True)
    sem7=models.FloatField(null=True)
    sem8=models.FloatField(null=True)
    def __str__(self):
        return self.usn

class sgpa_db(models.Model):
    sem=models.TextField(null=True)
    usn=models.TextField(max_length=10,null=True)
    m1=models.FloatField(null=True)
    m2=models.FloatField(null=True)
    m3=models.FloatField(null=True)
    m4=models.FloatField(null=True)
    m5=models.FloatField(null=True)
    m6=models.FloatField(null=True)
    m7=models.FloatField(null=True)
    m8=models.FloatField(null=True)
    m9=models.FloatField(null=True)
    sgpa=models.FloatField(null=True)
    def __str__(self):
        return self.usn