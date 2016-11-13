from rest_framework import serializers
from app.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    userName = serializers.CharField(max_length=20,required=True)
    password = serializers.CharField(max_length=100,required=True)
    code = serializers.CharField(max_length=20,required=True)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.userName = validated_data.get('userName',instance.userName)
        instance.password = validated_data.get('password',instance.password)
        instance.code = validated_data.get('code',instance.code)
        instance.save()
        return instance



