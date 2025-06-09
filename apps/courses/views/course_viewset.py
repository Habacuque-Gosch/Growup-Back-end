from rest_framework import generics
from apps.courses.models import Course, Review
from apps.courses.serializers import CourseSerializer, ReviewSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, AllowAny
from ..permissions import IsSuperuser, IsOwnerOrReadOnly
from rest_framework.pagination import PageNumberPagination



class CoursePagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().filter(available=True).order_by('-id')
    permission_classes = [IsAuthenticated]
    pagination_class = CoursePagination

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CourseSerializer
        return CourseSerializer

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
        Exemplo: /api/courses/bulk/?ids=3,5,7
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

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def enroll(self, request, pk=None):
        """
        Matricular usuário no curso
        """
        course = self.get_object()
        user = request.user
        if course.enrolled_users.filter(id=user.id).exists():
            return Response({'detail': 'Usuário já matriculado.'}, status=status.HTTP_400_BAD_REQUEST)
        course.enrolled_users.add(user)
        return Response({'detail': 'Matrícula realizada com sucesso.'})

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def unenroll(self, request, pk=None):
        """
        Cancelar matrícula do usuário no curso
        """
        course = self.get_object()
        user = request.user
        if not course.enrolled_users.filter(id=user.id).exists():
            return Response({'detail': 'Usuário não está matriculado.'}, status=status.HTTP_400_BAD_REQUEST)
        course.enrolled_users.remove(user)
        return Response({'detail': 'Matrícula cancelada com sucesso.'})

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def my_courses(self, request):
        """
        Listar cursos em que o usuário está matriculado
        """
        user = request.user
        courses = self.queryset.filter(enrolled_users=user)
        page = self.paginate_queryset(courses)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(courses, many=True)
        return Response(serializer.data)
    
# Viewset with mixins
class ReviewViewSet(mixins.ListModelMixin ,mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer