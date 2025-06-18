from rest_framework import serializers
from .models import Course, Category, Module, Lesson, Content, Review
from django.db.models import Avg




class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Review
        fields = '__all__'


# class AbsoluteImageField(serializers.ImageField):
#     def to_representation(self, value):
#         request = self.context.get('request')
#         photo_url = super().to_representation(value)

#         if request is not None:
#             return request.build_absolute_uri(photo_url)
#         return photo_url

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'title', 'order']

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'order']

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'content_type', 'text', 'video_url', 'order']

class LessonDetailSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'order', 'contents']

class ModuleDetailSerializer(serializers.ModelSerializer):
    lessons = LessonDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = ['id', 'title', 'order', 'lessons']

class CourseSerializer(serializers.ModelSerializer):
    # photo = AbsoluteImageField()
    category = serializers.SlugRelatedField(read_only=True, slug_field='name')
    reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    modules = ModuleDetailSerializer(many=True, read_only=True)
    is_enrolled = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'title', 'slug', 'content', 'duration', 'level', 'category', 'user', 'creation', 'update', 'available', 'modules', 'reviews', 'is_enrolled']

        def validate_slug(self, value):
            if self.instance:
                if Course.objects.exclude(id=self.instance.id).filter(slug=value).exists():
                    raise serializers.ValidationError('Esse slug já está em uso por outro curso.')
            else:
                if Course.objects.filter(slug=value).exists():
                    raise serializers.ValidationError('Esse slug já está em uso por outro curso.')
            return value
    
    def get_is_enrolled(self, obj):
        request = self.context.get('request', None)
        user = request.user if request else None

        if user and user.is_authenticated:
            return obj.enrolled_users.filter(id=user.id).exists()
        
        return False

    # NESTED RELATIONSHIP - 0-0
    # reviews = ReviewSerializer(many=True, read_only=True)
    # HYPERLINK RELATED FIELD - ;-;
    # reviews = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='review-detail')
    # PRIMARYKEY RELATED FIELD - :)

 