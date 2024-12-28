from rest_framework import serializers
from .models import Course, Review



class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Review
        fields = '__all__'


