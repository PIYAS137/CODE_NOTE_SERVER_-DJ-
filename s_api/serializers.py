from rest_framework import serializers
from s_api.models import StudentAuthCredential
from s_api.models import CodeModel

class StudentAuthCredential_Serializer(serializers.Serializer):
    s_id = serializers.IntegerField()
    s_secret = serializers.IntegerField()

    def create(self, validated_data):
        return StudentAuthCredential.objects.create(**validated_data)
    

class CodeModel_Serializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=10000)
    s_id = serializers.IntegerField()
    s_secret = serializers.IntegerField()
    date = serializers.CharField(max_length=40)
    course = serializers.CharField(max_length=40)

    def create(self, validated_data):
        return CodeModel.objects.create(**validated_data)
