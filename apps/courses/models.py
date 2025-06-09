from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime




class Base(models.Model):
    creation = models.DateTimeField(default=datetime.now)
    update = models.DateField(auto_now=True)
    available = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, default='')

    def __str__(self):
        return self.name

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
    category = models.ForeignKey(to=Category, on_delete=models.DO_NOTHING, null=True, blank=True, default='')
    enrolled_users = models.ManyToManyField(to=get_user_model(), related_name="enrolled_courses", blank=True)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, null=True, blank=False, related_name="user_owner")

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'
        ordering = ['-id']

    def __str__(self):
        return self.title

class Module(Base):
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Lesson(Base):
    module = models.ForeignKey(to=Module, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Content(Base):
    CONTENT_TYPES = [
        ('TEXT', 'Texto'),
        ('VIDEO', 'Vídeo'),
        ('QUIZ', 'Quiz'),
    ]

    lesson = models.ForeignKey(to=Lesson, on_delete=models.CASCADE, related_name='contents')
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES)
    text = models.TextField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.content_type} - {self.lesson.title}"

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
    
