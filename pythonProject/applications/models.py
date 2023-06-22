from django.db import models


class Applications(models.Model):
    Name = models.CharField('Имя клиента', max_length=50)
    Place = models.CharField('Место путешествия', max_length=50)
    PersonsCount = models.IntegerField('Количество людей')
    days = models.IntegerField('Количество дней')
    budget = models.IntegerField('Бюджет')
    text = models.TextField('Пожелания')
    mail = models.EmailField('Ваш Email')

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'