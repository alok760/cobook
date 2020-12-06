from django.db import models

# Create your models here.
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
    start_time = models.DateTimeField(
        null=False,
        blank=False,
        help_text='Enter the booking start time'
    )
    end_time = models.DateTimeField(
        null=False,
        blank=False,
        help_text='Enter the booking end time'
    )
    is_active = models.BooleanField(
        default=True,
        null=False,
        blank=False
    )
