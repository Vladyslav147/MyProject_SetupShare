from rest_framework import serializers
from .models import SetupPosts

class SetupPostsSelializer(serializers.ModelSerializer):
    class Meta:
        model = SetupPosts
        fields = '__all__'