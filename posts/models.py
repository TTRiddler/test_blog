from django.db import models
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from profiles.models import Contact


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created']

    def __str__(self):
        return '%s' % self.title

    def save(self, *args, **kwargs):
        try:
            author = self.author
            contacts = Contact.objects.filter(user_to=author)
            message = 'У %s новый пост!' % author
            mail_subject = 'Новый пост'
            for contact in contacts:
                to_email = contact.user_from.email
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
            super(Post, self).save(*args, **kwargs)
        except:
            super(Post, self).save(*args, **kwargs)


class PostRead(models.Model):
    who_read = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Читатель', related_name='readers')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    read = models.BooleanField(default=True, verbose_name='Прочитано')

    class Meta:
        verbose_name = 'Сзясь пост - подписчик'
        verbose_name_plural = 'Сзясь посты - подписчики'

    def __str__(self):
        return '%s %s' % (self.who_read.username, self.post.title)