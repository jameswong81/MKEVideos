from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Videos(models.Model):
    #user = models.ManyToManyField(User, default=1, on_delete=models.SET_DEFAULT)
    user = models.ForeignKey(User, default=1, verbose_name='User', on_delete=models.SET_DEFAULT)
    video_filename = models.FileField(upload_to='Videos/')

    def __str__(self):
        return '{} {}'.format(self.user.username, self.video_filename)

