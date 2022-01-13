from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class WorkSpace(models.Model):
    WORKSPACE_CITY_LOCATIONS = (
        (1, 'Moscow'),
        (2, 'SPB'),
        (3, 'Krasnodar')
    )
    WORKSPACE_TYPES = (
        (1, 'budgetary'),
        (2, 'standart'),
        (3, 'business'),
    )

    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Name', db_index=True, max_length=40)
    address = models.CharField(verbose_name='address', db_index=True, max_length=50)
    city_location = models.IntegerField(choices=WORKSPACE_CITY_LOCATIONS)
    type = models.IntegerField(verbose_name='Type', choices=WORKSPACE_TYPES)

    def __str__(self):
        return f'"{self.name}", {self.WORKSPACE_CITY_LOCATIONS[self.city_location][1]} ' \
               f'({self.address})'
