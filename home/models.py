from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=600)
    message=models.TextField()

    def __str__(self):
        return self.full_name

class ContactInformation(models.Model):
    address = models.CharField(max_length=300)
    street_address = models.CharField(max_length=500)
    contact_num = models.CharField(max_length=300)
    time = models.CharField(max_length=300)
    email = models.CharField(max_length=600)

    def __str__(self):
        return self.address

class Testomonials(models.Model):
    name = models.CharField(max_length=300)
    designation= models.CharField(max_length=500)
    comment = models.TextField()
    image = models.TextField()


    def __str__(self):
        return self.name

class Servicesinfo(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    logo = models.CharField(max_length=400)

    def __str__(self):
        return self.title
