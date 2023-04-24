from django.db import models

# Create your models here.

class web(models.Model):
    name = models.CharField(max_length=225)
    address = models.CharField(max_length=1000) 
    email = models.CharField(max_length=225)
    form_no = models.IntegerField()
    current_date = models.CharField(max_length=225)
    s = models.IntegerField()
    cdate = models.CharField(max_length=225)
    cn1 = models.CharField(max_length=20)
    cn2 = models.CharField(max_length=20)
    sex = models.CharField(max_length=225)
    course = models.CharField(max_length=225)#Course
    fa = models.IntegerField()#fees paid
    ia= models.IntegerField()#installment amount
    d = models.IntegerField()#Discount
    apf = models.IntegerField()#Addmission fees paid
    doi = models.IntegerField()#date of installment
    rf = models.IntegerField()#Remaining Fees
    tfp = models.IntegerField()#total Fees Paid
    ino = models.IntegerField()#installment number
class login(models.Model):
    UN=models.CharField(max_length=225)
    PW=models.CharField(max_length=225)