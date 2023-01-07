from django.db import models

# Create your models here.

class DocumentChoices(models.TextChoices):
    CC = "CÉDULA DE CIUDADANÍA"
    PP = "PASAPORTE"
    CE = "CÉDULA DE EXTRANJERÍA"


class Person(models.Model):
    document_type = models.CharField(max_length=255, choices=DocumentChoices.choices, default=DocumentChoices.CC)
    document = models.CharField(max_length=50, unique=True)
    names = models.CharField(max_length=255)
    last_names = models.CharField(max_length=255)
    hobbie = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
