from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rel_from_set', verbose_name='Кто подписан')
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rel_to_set', verbose_name='На кого подписан')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    class Meta:
        verbose_name = 'Связь'
        verbose_name_plural = 'Связи'
        ordering = ['-created']

    def __str__(self):
        return '%s подписан на %s' % (self.user_from, self.user_to)

#Динамически добавляет поле following в класс User
User.add_to_class('following', models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False))