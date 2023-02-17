from rest_framework import serializers
from .models import *


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

    def validate(self, data):
        if len(data.get('comment_text')) < 100:
            raise serializers.ValidationError('Отзыв не может быть менее 100 символов')
        if data.get('car_key') == None or type(data.get('car_key')) == str:
            raise serializers.ValidationError('Необходимо указать ID автомобиля')

        return data

class CarSerializer(serializers.ModelSerializer):

    developer = serializers.SerializerMethodField()
    comments = CommentSerializer(many = True)
    comments_count = serializers.SerializerMethodField()

    def get_developer(self, obj):
        return obj.developer_key.name
    def get_comments_count(self, obj):
        return obj.comments.count()

    class Meta:
        model = Car
        fields = ['name', 'developer', 'comments_count', 'comments']


class CommentCountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        exclude = ('comment_text', 'id', 'author_email', 'date_created', 'car_key')

class DeveloperNestedSerializer(serializers.ModelSerializer):

    developer = serializers.SerializerMethodField()
    comments = CommentCountSerializer(many = True)
    comments_count = serializers.SerializerMethodField()

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        request = self.context.get('request')
        if request is not None and not request.parser_context.get('kwargs'):
            fields.pop('comments', None)
            fields.pop('developer', None)
        return fields

    def get_developer(self, obj):
        return obj.developer_key.name

    def get_comments_count(self, obj):
        return obj.comments.count()

    class Meta:
        model = Car
        fields = ['name', 'developer', 'comments_count', 'comments']


class DeveloperSerializer(serializers.ModelSerializer):

    cars = DeveloperNestedSerializer(many=True)
    country = serializers.SerializerMethodField()

    def get_country(self, obj):
        return obj.country_key.name


    class Meta:
        model = Developer
        fields = ['name', 'country', 'cars']


class CountrySerializer(serializers.ModelSerializer):
    developers = serializers.SlugRelatedField(many = True, slug_field = 'name', read_only = True)
    class Meta:

        model = Country
        fields = ['name', 'developers']