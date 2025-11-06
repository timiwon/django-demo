from rest_framework import serializers

from .models import Article

class UserSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    username = serializers.CharField()
    email = serializers.CharField()

class ArticleSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    #title = serializers.CharField(required=False)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'owner']
        depth = 1

class ArticleListRequestSerializer(serializers.Serializer):
    page = serializers.IntegerField(default=1)
    per_page = serializers.IntegerField(default=10)
    owner_only = serializers.BooleanField(default=False)
