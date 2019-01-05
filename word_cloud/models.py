from django.db import models


class Website(models.Model):
    name         = models.CharField(max_length=500)
    request_time = models.DateTimeField('requested time')
    def __str__(self):
        return self.name

class Word(models.Model):
    website   = models.ForeignKey(Website, default=1, on_delete=models.CASCADE)
    key       = models.CharField(max_length=200)
    word      = models.CharField(max_length=200)
    frequency = models.IntegerField(default=0)

    def __str__(self):
        return self.word

