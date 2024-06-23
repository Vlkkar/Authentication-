from django.db import models


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=32)
    code = models.IntegerField()

    def __str__(self):
        return self.username


# Create your models here.
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


