from django.db import models
from workspace.models import WorkSpace
from django.contrib.auth import get_user_model
User = get_user_model()


class Booking(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    workspace = models.ForeignKey(WorkSpace, verbose_name='Work Space', on_delete=models.CASCADE)
    beginning = models.DateTimeField(null=True, default=None, verbose_name=('Beginning time'))
    ending = models.DateTimeField(null=True, default=None, verbose_name=('Ending time'))
