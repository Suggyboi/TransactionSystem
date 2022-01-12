import uuid
from django.db import models
from django.urls import reverse
from accounts.models import CustomUser


class Category(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    name = models.CharField(max_length= 250, unique = True)
    image = models.ImageField(upload_to = 'category', null = True, blank = True)
    #events = models.ManyToManyField('Event') 

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def get_absolute_url(self):
        return reverse('shop:events_by_category', args=[self.id])
    
    def __str__(self):
        return self.name

class Event(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False 
    )

    # status_options = [
    #     ('Draft','Draft'),
    #     ('Posted','Posted')
    # ]

    title = models.CharField(max_length = 25, unique = True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    price = models.DecimalField(max_digits = 10, decimal_places = 2, null=True)
    organiser = models.ForeignKey(CustomUser, on_delete = models.CASCADE, null=True)
    venue = models.TextField()
    startdate = models.DateField(null=True)
    starttime = models.TimeField(null=True)
    enddate = models.DateField(null=True)
    endtime = models.TimeField(null=True)
    image = models.ImageField(upload_to = 'product', null = True, blank = True)
    stock = models.IntegerField(null=True)
    available = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True)
    updated = models.DateTimeField(auto_now = True, blank = True, null = True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'event'
        verbose_name_plural = 'events'

    def get_absolute_url(self):
        return reverse('shop:event_detail', args=[self.category.id, self.id])
    
    def __str__(self):
        return self.title

