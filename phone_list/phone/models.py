from django.db import models


class Contact(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    home = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
