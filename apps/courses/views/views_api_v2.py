from rest_framework import generics
from apps.courses.models import Course, Review
from apps.courses.serializers import CourseSerializer, ReviewSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, AllowAny
from ..permissions import IsSuperuser, IsOwnerOrReadOnly




class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().filter(available=True).order_by('-id')
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsOwnerOrReadOnly()]
        return [IsAuthenticated()]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def bulk(self, request):
        """
        Retorna múltiplos cursos baseado em uma lista de IDs:
        /api/courses/bulk/?ids=3,5,7
        """
        ids_param = request.query_params.get('ids', '')
        if not ids_param:
            return Response({"detail": "Parâmetro 'ids' é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            ids = [int(id_str) for id_str in ids_param.split(',') if id_str.isdigit()]
        except ValueError:
            return Response({"detail": "IDs inválidos."}, status=status.HTTP_400_BAD_REQUEST)

        cursos = self.queryset.filter(id__in=ids)
        serializer = self.get_serializer(cursos, many=True)
        return Response(serializer.data)

    # @action(detail=True, methods=['GET'])
    # def reviews(self, request, pk=None):

    #     self.pagination_class.page_size = 50
    #     courses = Review.objects.filter(course_id=pk)
    #     page = self.paginate_queryset(courses)

    #     if page is not None:
    #         serializer = ReviewSerializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)

    #     serializer = ReviewSerializer(Review.all(), many=True)
    #     return Response(serializer.data)

# Viewset with mixins
class ReviewViewSet(mixins.ListModelMixin ,mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer