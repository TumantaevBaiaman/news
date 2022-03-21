from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    content = models.TextField()
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Пост'
        verbose_name = 'Пост'


class Option(models.Model):
    name = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Вариант'
        verbose_name = 'Вариант'


class Grade(models.Model):
    grade = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.grade)

    class Meta:
        verbose_name_plural = 'Оценка'
        verbose_name = 'Оценка'


class We(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    grate = models.ForeignKey(Grade, on_delete=models.CASCADE)
    content = models.TextField()

    class Meta:
        verbose_name_plural = 'Отзыв'
        verbose_name = 'Отзывы'


    def __str__(self):
        return '{} - {} - {}'.format(self.post, self.option, self.grate)
