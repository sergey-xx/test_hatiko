from rest_framework import serializers


class RequestCodeSerializer(serializers.Serializer):
    code = serializers.IntegerField()
