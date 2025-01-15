import random
import string

from rest_framework import serializers

from .models import VPS
from .utils import MAX_UID_VALUE_SIZE


class VPSCreationSerializer(serializers.ModelSerializer):
    """Сериализатор для создания новых виртуальных серверов."""
    uid = serializers.CharField(max_length=32)
    cpu = serializers.IntegerField(required=True)
    ram = serializers.IntegerField(required=True)
    hdd = serializers.IntegerField(required=True)
    status = serializers.ChoiceField(
        max_length=7,
        choices=["Started", "Blocked", "Stopped"],
        )

    class Meta:
        model = VPS
        fields = ('id', 'uid', 'cpu', 'ram', 'hdd', 'status')

    def create(self, validated_data):
        random_values = string.ascii_lowercase + string.digits
        uid = ''.join(
            random.choice(random_values) for _ in range(MAX_UID_VALUE_SIZE)
            )
        if VPS.objects.filter(uid=uid).exists():
            raise serializers.ValidationError(
                "Ошибка присваивания уникального uid. Попробуйте еще раз."
            )

        vps = VPS.objects.create(
            uid=uid,
            cpu=validated_data.get('cpu'),
            ram=validated_data.get('ram'),
            hdd=validated_data.get('hdd'),
            status=validated_data.get('status')
        )

        return vps


class VPSInfoSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра информации о виртуальных серверах."""

    class Meta:
        model = VPS
        fields = ('id', 'uid', 'cpu', 'ram', 'hdd', 'status')
