from django.db import models
from django.contrib.postgres.fields import ArrayField


class Expert(models.Model):
    name = models.CharField(max_length=40)
    personal_website_url = models.CharField(max_length=100)
    shortened_personal_website_url = models.CharField(max_length=100)
    friendships = ArrayField(models.CharField(max_length=40), null=True)

class Friendships(models.Model):
    expert_id_001 = models.IntegerField()
    expert_id_002 = models.IntegerField()
