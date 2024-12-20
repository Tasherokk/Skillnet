from django.db import models
from users.models import User

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["created_at"]),  # Индекс для сортировки курсов по дате создания
        ]

    def __str__(self):
        return self.title


class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="topics")
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        indexes = [
            models.Index(fields=["course"]),  # Индекс для фильтрации по курсу
        ]

    def __str__(self):
        return self.title


class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["course"]),  # Индекс для фильтрации комментариев по курсу
            models.Index(fields=["author"]),  # Индекс для фильтрации комментариев по автору
            models.Index(fields=["created_at"]),  # Индекс для сортировки комментариев по времени
        ]

    def __str__(self):
        return f'Comment by {self.author.username} on {self.course.title}'