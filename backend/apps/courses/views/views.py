# from rest_framework.views import APIView
# from rest_framework import status
from rest_framework import generics
from apps.courses.models import Course, Review
from apps.courses.serializers import CourseSerializer, ReviewSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response



class CoursesAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    
class ReviewsAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        id = self.kwargs.get('review_pk')
        if id:
            return self.queryset.filter(review_id=id)
        return self.queryset.all()
    
    
class ReviewAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_object(self):
        id_course = self.kwargs.get('course_pk')
        id_review = self.kwargs.get('review_pk')

        if id_course:
            return get_object_or_404(self.get_queryset(), course_id=id_course, pk=id_review)
        
        return get_object_or_404(self.get_queryset(), pk=id_review)



