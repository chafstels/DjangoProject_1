from django.db import models

# Create your models here.

"""
1. Модель Task (Задача):
• Поле title (Заголовок) типа CharField с максимальной длиной
100 символов.
• Поле description (Описание) типа TextField.
• Поле status (Статус) типа BooleanField со значением по
умолчанию False.
• Поле created_at (Дата создания) типа DateTimeField с
автоматическим добавлением значения при создании
записи.
2. Модель Project (Проект):
• Поле name (Название проекта) типа CharField с максимальной
длиной 100 символов.
• Поле description (Описание проекта) типа TextField. •
Поле start_date (Дата начала проекта) типа DateField. •
Поле end_date (Дата окончания проекта) типа DateField.
3. Модель Comment (Комментарий):
• Поле task (Задача) типа ForeignKey, связано с моделью Task. •
Поле user (Пользователь) типа ForeignKey, связано с моделью
User.
• Поле content (Содержание комментария) типа TextField. •
Поле created_at (Дата создания комментария) типа
DateTimeField с автоматическим добавлением значения при
создании записи."""


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task