from django.db import models
from apps.utils.models import Timestamps

class Certificate(Timestamps,
                  models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
