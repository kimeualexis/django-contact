from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=45)
    is_male = models.BooleanField(default=True)
    cover = models.FileField()
    email = models.EmailField()
    telephone = models.CharField(max_length=12)
    relation = models.CharField(max_length=45)
    residence = models.CharField(max_length=50)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('users:contact-index')





