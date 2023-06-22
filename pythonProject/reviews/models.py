from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

size = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(5)])


class FeedBack(models.Model):
    Name = models.CharField('Имя клиента', max_length=50)
    Place = models.CharField('Место путешествия', max_length=50)
    full_text = models.TextField('Отзыв')
    date = models.DateField('Дата путешествия')
    score = models.IntegerField('Оценка', validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
