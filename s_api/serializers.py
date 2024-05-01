from rest_framework import serializers
from s_api.models import StudentAuthCredential

class StudentAuthCredential_Serializer(serializers.Serializer):
    s_id = serializers.IntegerField()
    s_secret = serializers.IntegerField()

    def create(self, validated_data):
        return StudentAuthCredential.objects.create(**validated_data)