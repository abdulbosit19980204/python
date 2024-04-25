from rest_framework import serializers

from blog.models import Post, Comment, MyUser, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['posts'] = PostSerializer(Post.objects.filter(category_id=instance.id), many=True).data
        return data


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['comments'] = CommentSerializer(Comment.objects.filter(post_id=instance.id), many=True).data
        return data


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['posts'] = PostSerializer(Post.objects.filter(author__id=instance.id), many=True).data
        return data
