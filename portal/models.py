from django.db import models
from django.db.models import F

# Create your models here.

class Phone(models.Model):
    phonenum = models.CharField(max_length=15)
    PHONE_STATUS = (
        ('DG', 'Danger'),
        ('NW', 'New'),
        ('NM', 'Normal')
    )
    status = models.CharField(max_length=2, choices=PHONE_STATUS, default='NW')
    # count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phonenum

class Report(models.Model):
    body = models.TextField()
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    REPORT_TYPE = (
        ('SMS', 'SMS'),
        ('CALL', 'Call')
    )
    type = models.CharField(max_length=4, choices=REPORT_TYPE, null=True)

    def __str__(self):
        return "Report number " + str(self.phone)

class Category(models.Model):
    categoryname = models.CharField(max_length=30)
    report = models.ManyToManyField(Report)

    def __str__(self):
        return self.categoryname