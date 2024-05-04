from rest_framework import serializers

from .models import Post, Category, CommentPost, FavoritePost, LikePost, MyUser, Notification


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['posts_count'] = Post.objects.filter(category=instance).count()
        data['posts'] = PostSerializer(Post.objects.filter(category=instance), many=True).data

        return data


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    # darsda save qilingan
    def save(self, **kwargs):
        request = self.context['request']
        # request tookendan oladi shuning uchun token qoshilmasa {"author":["This field is required."]}
        user = MyUser.objects.filter(user_id=request.user.id).first()
        self.validated_data['author'] = user
        return super().save(**kwargs)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['comments_count'] = CommentPost.objects.filter(post=instance).count()
        data['comments'] = CommentSerializer(CommentPost.objects.filter(post=instance), many=True).data
        return data


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentPost
        fields = '__all__'

    def save(self, **kwargs):
        user = self.context['request'].user
        print(user)
        return super().save(**kwargs)


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['posts'] = PostSerializer(Post.objects.filter(author=instance), many=True).data
        return data
