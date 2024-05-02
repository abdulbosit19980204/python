from rest_framework import serializers

from blog.models import MyUser, Post
from blog.serializers import PostSerializer
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['posts'] = PostSerializer(Post.objects.filter(author=instance), many=True).data
        return data
