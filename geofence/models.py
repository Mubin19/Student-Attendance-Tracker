from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from django.forms import CharField
# Create your models here.
CLASS_CHOICES=(
    ('MCA1','MCA1'),
    ('MBA1','MBA1'),
    ('MCA2','MCA2'),
    ('MBA2','MBA2'),
)
DIVISION_CHOICES=(
    ('Codewarroiers','Codewarroiers'),
    ('Technocrats','Technocrats'),
)
class Student(models.Model):
    name=models.CharField(max_length=200,null=False,blank=False)
    classs=models.CharField(choices=CLASS_CHOICES,max_length=50)
    division=models.CharField(choices=DIVISION_CHOICES,max_length=50)
    rollno=models.IntegerField()
    mobile=models.IntegerField()
    macaddress=models.CharField(max_length=200,null=False,blank=False)
    parentmobile=models.IntegerField()
    email=models.EmailField()
    def _str_(self):
        return str(self.id)

ENTER_CLASS=(
    ('MBA','MBA'),
    ('MCA','MCA'),
)

class Inout(models.Model):
    classs=models.CharField(choices=ENTER_CLASS,max_length=50)
    intime=models.TimeField()
    outtime=models.TimeField()
    def _str_(self):
        return str(self.id)

class Studententry(models.Model):
    date=models.CharField(max_length=50,null=False,blank=False)
    time=models.CharField(max_length=50,null=False,blank=False)
    macadd=models.CharField(max_length=200,null=False,blank=False)
    def _str_(self):
        return str(self.id)
    
