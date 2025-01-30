from rest_framework import serializers

from utils.imei_checker import IMEI


class RequestCodeSerializer(serializers.Serializer):
    code = serializers.CharField(min_length=15, max_length=15)

    def validate_code(self, value):
        imai = IMEI(value)
        is_valid, text = imai.validate()
        if not is_valid:
            raise serializers.ValidationError(text)
        return value
