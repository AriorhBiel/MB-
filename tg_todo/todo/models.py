from django.db import models
from django.utils.translation import gettext_lazy as _

class User(models.Model):
    telegram = models.CharField(_(u"Пользователь"), max_length=128)

    def __str__(self):
        return self.telegram
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Record(models.Model):
    title = models.CharField(_(u"Заголовок"), max_length=128)
    text = models.CharField(_(u"Текст"), max_length=2000)
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Date(models.Model):
    record = models.ForeignKey(Record, on_delete = models.CASCADE)
    timer = models.DateField(_(u"Время"), max_length=64)

    def __str__(self):
        return str(self.timer)
    
    class Meta:
        verbose_name = 'Напоминалка'
        verbose_name_plural = 'Напоминалки'