from rest_framework import generics
from apps.courses.models import Course, Review
from apps.courses.serializers import CourseSerializer, ReviewSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from ..permissions import IsSuperuser



class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('-id')
    serializer_class = CourseSerializer
    permission_classes = (IsSuperuser, permissions.DjangoModelPermissions,)

    @action(detail=True, methods=['GET'])
    def reviews(self, request, pk=None):

        self.pagination_class.page_size = 50
        courses = Review.objects.filter(course_id=pk)
        page = self.paginate_queryset(courses)

        if page is not None:
            serializer = ReviewSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ReviewSerializer(Review.all(), many=True)
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