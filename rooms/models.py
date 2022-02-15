from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.TimeStampedModel):
    """Abstract Item"""
    name = models.CharField(max_length=80)
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """RoomType Model Definition"""
    
    class Meta:
        verbose_name = 'Room Type'
        ordering = ['-created']


class Amenity(AbstractItem):
    """Amenity Model Definition"""
    
    class Meta:
        verbose_name_plural = 'Amenities'


class Facility(AbstractItem):
    """Facility Model Definition"""
    
    class Meta:
        verbose_name_plural = 'Facilities'


class HouseRule(AbstractItem):
    """HouseRule Model Definition"""
    
    class Meta:
        verbose_name = 'House Rule'


class Photo(core_models.TimeStampedModel):
    """Photo Model Definition"""
    
    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey('Room', on_delete=models.CASCADE) # string because python reads from top to bottom
    
    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):
    """Room Model Definition"""
    
    name = models.CharField(max_length=140) # required
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80) # required
    price = models.IntegerField() # required
    address = models.CharField(max_length=140) # required
    guests = models.IntegerField()
    bedrooms = models.IntegerField()
    beds = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField() # from 0 to 24
    check_out = models.TimeField() # from 0 to 24
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey('users.User', on_delete=models.CASCADE) # or user_models.User
    room_type = models.ForeignKey('RoomType', on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField('Amenity', blank=True)
    facilities = models.ManyToManyField('Facility', blank=True)
    house_rules = models.ManyToManyField('HouseRule', blank=True)
    
    def __str__(self):
        return self.name
    