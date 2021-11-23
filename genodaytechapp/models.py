from django.db import models
from django.conf import settings
from django.db.models.fields import CharField
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

class contact(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.EmailField(max_length=200,null=True)
    number=models.IntegerField(null=True)
    message=models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.name


class ChatBox(models.Model):
    nameC=models.CharField(max_length=100)
    domainName=models.CharField(max_length=150)
    companyName=models.CharField(max_length=150)
    emailC=models.EmailField(max_length=150)

    def __str__(self):
        return self.nameC

