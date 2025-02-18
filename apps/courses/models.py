from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class Base(models.Model):
    creation = models.DateField(auto_created=True)
    update = models.DateField(auto_now=True)
    available = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Course(Base):
    title = models.CharField(max_length=255, blank=False, null=False, default='')
    slug = models.CharField(max_length=100, unique=True)

    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        related_name="user_owner",
    )

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['-id']

    def __str__(self):
        return self.title
    

class Review(Base):
    course = models.ForeignKey(Course, related_name='reviews', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.CharField(max_length=255, blank=True, default='')
    review = models.DecimalField(max_digits=2, decimal_places=1)
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        related_name="user_review",
    )

    class Meta:
        verbose_name = 'review'
        verbose_name_plural = 'reviews'
        unique_together = ['email', 'course']
        ordering = ['-id']

    def __str__(self):
        return f'{self.name} evaluated the course {self.course} with a gradereview {self.review}'