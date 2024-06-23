from django.db import models

'''''
class Users(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=32)
    code = models.IntegerField()

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
'''''
# Create your models here.
from django.db import connections
from django.db.utils import OperationalError

try:
    connection = connections['default']
    cursor = connection.cursor()
    print("Успешное подключение к базе данных!")
except OperationalError as e:
    print("Ошибка подключения к базе данных:", e)