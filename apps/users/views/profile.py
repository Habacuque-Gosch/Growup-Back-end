from ..models import UserProfile
from apps.courses.models import Course
from ..serializers import ProfileSerializer
from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
User = get_user_model()





class ProfileViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get', 'patch'], url_path='me')
    def me(self, request):
        try:
            current_user = request.user
            profile =  UserProfile.objects.get(user=current_user)
            
            if request.method == 'GET':
                serializer = ProfileSerializer(profile)
                return Response(serializer.data)

            elif request.method == 'PATCH':
                serializer = ProfileSerializer(profile, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except UserProfile.DoesNotExist:
            return Response({"detail":"Perfil não encontrado"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['post'], url_path='save-course')
    def save_course(self, request):
        try:
            profile = UserProfile.get_profile(request.user.id)
            course_id = request.data.get("course_id")

            if not course_id:
                return Response({"detail": "ID do course é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)
            
        except UserProfile.DoesNotExist:
            return Response({"detail": "Profile do usuário não existe"}, status=status.HTTP_404_NOT_FOUND)

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({"detail": "Course não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        profile.courses_save.add(course)
        return Response({"detail": "Course salvo com sucesso."}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['delete'], url_path='remove-course_id')
    def Course(self, request, pk=None):
        try:
            profile = UserProfile.get_profile(request.user.id)
        except UserProfile.DoesNotExist:
            return Response({"detail": "Profile do usuário não existe"}, status=status.HTTP_404_NOT_FOUND)

        try:
            course = Course.objects.get(id=pk)
        except Course.DoesNotExist:
            return Response({"detail": "Course não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        profile.courses_save.remove(course)
        return Response({"detail": "Course removido com sucesso."}, status=status.HTTP_200_OK)




