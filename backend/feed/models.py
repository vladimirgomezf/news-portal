import datetime
from django.utils.timezone import now
from django.db import models

methods_choices = (
    ('post', 'POST'),
    ('get', 'GET'),
    ('delete', 'DELETE'),
    ('put', 'PUT')
)


class News(models.Model):
    author = models.CharField('Author', max_length=75)
    head = models.CharField('Headline', max_length=75)
    resume = models.CharField('Resume', max_length=250)
    content = models.CharField('Content', max_length=2500)
    publisedDate = models.DateField('Published At', default=now)


class LogRegistry(models.Model):
    method = models.CharField('Method', max_length=10, choices=methods_choices)
    url = models.URLField('URL')
    response = models.BooleanField(default=False)
