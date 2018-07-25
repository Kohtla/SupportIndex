from django.db import models
from django.urls import reverse

# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length = 100)
    def_first = models.CharField(max_length =300)
    def_second = models.CharField(max_length= 1500)
    #tech_stack
    image_logo = models.FileField(null = True, blank=True)
    image_first = models.FileField(null=True, blank=True)
    image_second = models.FileField(null=True, blank=True)
    gif = models.FileField(null=True,blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('forum:detail', kwargs={'pk':self.pk})