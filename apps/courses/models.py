from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime




class Base(models.Model):
    creation = models.DateTimeField(default=datetime.now)
    update = models.DateField(auto_now=True)
    available = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Course(Base):

    LEVELS = [
        ("INICIANTE","Iniciante"),
        ("INTERMEDIÁRIO","Intermediário"),
        ("AVANÇADO","Avançado"),
    ]
    title = models.CharField(max_length=255, blank=False, null=False, default='')
    slug = models.CharField(max_length=100, unique=True)
    content = models.TextField(max_length=750, default='')
    # photo = models.ImageField(upload_to="course/thumbnail/%Y/%m/%d/", blank=True, null=True)
    duration = models.IntegerField(default=5, blank=False)
    level = models.CharField(max_length=100, choices=LEVELS, blank=False, null=False, default='INICIANTE')
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, null=True, blank=False, related_name="user_owner")

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'
        ordering = ['-id']

    def __str__(self):
        return self.title

class Review(Base):
    course = models.ForeignKey(Course, related_name='reviews', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
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
        unique_together = ['course']
        ordering = ['-id']

    def __str__(self):
        return f'{self.name} evaluated the course {self.course} with a gradereview {self.review}'
    
