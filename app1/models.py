from django.db import models


class employee(models.Model):
    empid=models.IntegerField()
    name=models.CharField(max_length=50)
    DO_Birth=models.CharField(max_length=30)
    DO_Joining=models.CharField(max_length=67)
    DO_Anniversary=models.CharField(max_length=59)
    Email=models.EmailField(max_length=50)


    def __str__(self):
        return  self.name


