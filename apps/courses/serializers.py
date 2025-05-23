from rest_framework import serializers
from .models import Course, Review
from django.db.models import Avg




class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Review
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    # NESTED RELATIONSHIP - 0-0
    # reviews = ReviewSerializer(many=True, read_only=True)

    # HYPERLINK RELATED FIELD - ;-;
    # reviews = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='review-detail')
 
    # PRIMARYKEY RELATED FIELD - :)
    reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # media_review = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'title', 'slug', 'content', 'user', 'creation', 'update', 'available', 'reviews',]

        def validate_slug(self, value):
            if self.instance:
                if Course.objects.exclude(id=self.instance.id).filter(slug=value).exists():
                    raise serializers.ValidationError('Esse slug já está em uso por outro curso.')
            else:
                if Course.objects.filter(slug=value).exists():
                    raise serializers.ValidationError('Esse slug já está em uso por outro curso.')
            return value

    # def get_media_review(self, obj):
    #     media = obj.reviews.aggregate(Avg('review')).get('review__avg')

    #     if media is None:
    #         return 0
    #     return round(media*2)/2

 