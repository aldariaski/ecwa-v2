from django.db import models

# Create your models here.

class Journal(models.Model):
    usernamezz = models.CharField(max_length=90)
    totals = models.IntegerField(default=0)
    recordtotals = models.IntegerField(default=0)

    def __str__(self):
        return self.usernamezz

class Record(models.Model):
    recordid = models.IntegerField(default=None)
    typezz = models.CharField(max_length=1)
    values = models.IntegerField(default=0)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)

    def __str__(self):
        return self.typezz
    
    def value(self):
        return self.values