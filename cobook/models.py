from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BaseModel(models.Model):
    """
    This is an abstract model to be used by all the other models.
    This provides 2 important timestamp fields - Created and Modified
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Cowork(BaseModel):
    """
    This stores details of the Co-Working Space
    """

    ##User who owns the space
    user = models.ForeignKey(
        User,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        null=False,
        blank=False,
        max_length=100,
        help_text='Enter the name of the room'
    )
    capacity = models.PositiveIntegerField(
        null=False,
        blank=False,
        help_text='Enter the number of room the Coworking space have'
    )

    zipcode = models.PositiveIntegerField(
        null=False,
        blank=False,
        help_text='Enter the number of room the Coworking space have'
    )

    start_time = models.TimeField(
        default='09:00:00',
        null=False,
        blank=False,
        help_text='Enter when the coworking space opens'
    )
    end_time = models.TimeField(
        default='20:00:00',
        null=False,
        blank=False,
        help_text='Enter the closing time of coworking space'
    )

    def __str__(self):
        return self.name


class Room(BaseModel):
    """
    This stores details of conference rooms available
    """
    name = models.CharField(
        null=False,
        blank=False,
        max_length=100,
        help_text='Enter the name of the room'
    )
    capacity = models.PositiveIntegerField(
        null=False,
        blank=False,
        help_text='Enter the number of person\'s the room can accommodate'
    )

    cowork = models.ForeignKey(
        Cowork,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.cowork.name + ' - ' + self.name


class Booking(BaseModel):
    """
    This stores details of bookings of the conference rooms
    """
    user = models.ForeignKey(
        User,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        Room,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    start_time = models.TimeField(
        null=False,
        blank=False,
        help_text='Enter the booking start time'
    )
    end_time = models.TimeField(
        null=False,
        blank=False,
        help_text='Enter the booking end time'
    )

    date = models.DateField(
        null=False,
        blank=False,
        help_text='Enter the booking end time'
    )
    is_active = models.BooleanField(
        default=True,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.room.name + ' - ' + str(self.date)
