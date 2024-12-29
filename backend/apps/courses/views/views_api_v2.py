from rest_framework import generics
from apps.courses.models import Course, Review
from apps.courses.serializers import CourseSerializer, ReviewSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response




class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['GET'])
    def reviews(self, request, pk=None):
        course = self.get_object()
        serializer = ReviewSerializer(course.reviews.all(), many=True)
        return Response(serializer.data)


''' Viewset defaut layout
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
'''

# Viewset with mixins
class ReviewViewSet(mixins.ListModelMixin ,mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer