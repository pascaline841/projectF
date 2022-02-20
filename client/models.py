from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.email}"
