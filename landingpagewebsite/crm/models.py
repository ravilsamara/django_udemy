from django.db import models

# Create your models here.
class StatusCrm(models.Model):
    status_name = models.CharField(max_length=200,verbose_name='Название статуса')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'



class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True, verbose_name='дата')
    order_name = models.CharField(max_length=200, verbose_name="имя")
    order_phone = models.CharField(max_length=200, verbose_name="телефон")
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ComentCrm(models.Model):
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE,verbose_name='Заявка')
    comment_text = models.TextField(verbose_name='Текст Комментария')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'