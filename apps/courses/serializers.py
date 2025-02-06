from rest_framework import serializers
from .models import Course, Review



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

    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'slug',
            'creation',
            'update',
            'available',
            'reviews'
        )


