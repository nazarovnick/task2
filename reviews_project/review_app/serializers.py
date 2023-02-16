from rest_framework import serializers
from .models import *


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

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


class DeveloperSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True)
    country = serializers.SerializerMethodField()

    def get_country(self, obj):
        return obj.country_key.name

    class Meta:
        model = Developer
        fields = ['name', 'country', 'cars']

class OnlyDeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = ['name']



class CountrySerializer(serializers.ModelSerializer):

    developers = serializers.SlugRelatedField(many = True, slug_field = 'name', read_only = True)
    class Meta:

        model = Country
        fields = ['name', 'developers']