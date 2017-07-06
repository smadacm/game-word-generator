from django.db import models
from django.db.models.aggregates import Count
from random import randint

# Create your models here.
class Category(models.Model):
    name = models.CharField('Name', max_length=255)

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.__unicode__()

class Word(models.Model):
    word = models.CharField('Word', max_length=255)
    category = models.ForeignKey(Category, verbose_name='Category')

    @classmethod
    def random(cls, category):
        collection = cls.objects.filter(category=category)
        count = collection.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return collection.filter(category=category)[random_index]

    def __unicode__(self):
        return self.word
    def __str__(self):
        return self.__unicode__()
