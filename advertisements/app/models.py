from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    auction = models.BooleanField(default=False, verbose_name='Торг')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image = models.ImageField("Изображение", upload_to='advertisements/')

    @admin.display(description='дата создания')
    def created_date(self):
        from django.utils import timezone
        from django.utils.html import format_html

        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html('<span>Сегодня в {}</span>',created_time)
        return self.created_at.strftime("%d.%m.%y в %H:%M:%S")
    
    @admin.display(description='дата обновления')
    def updated_date(self):
        from django.utils import timezone
        from django.utils.html import format_html

        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html('<span style="color:#00FF00;">Сегодня в {}</span>',updated_time)
        return self.updated_at.strftime("%d.%m.%y в %H:%M:%S")

    @admin.display(description='изображениe')
    def img_output(self):
        from django.utils.html import format_html
        if self.image:
            return format_html('<img src="{}"  style="width: 50px;">', self.image.url)

    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'
    
    class Meta:
        db_table = 'advertisements'

    def get_absolute_url(self):
        return reverse('advertisement', kwargs={'pk': self.pk})