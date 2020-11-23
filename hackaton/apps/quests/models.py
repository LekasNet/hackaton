from django.db import models

class Quest(models.model):
    pass

class Card(models.model):
    card_title = models.CharField("name")
    card_link = models.CharField("link")
    card_sort_age= models.IntegerField("age_group")
    card_sort_interests = models.IntegerField("inter_group")