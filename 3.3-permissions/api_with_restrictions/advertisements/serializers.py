from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from advertisements.models import Advertisement, Favorite


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
        )


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = "__all__"

    def create(self, validated_data):
        """Метод для создания"""
        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        user = self.context["request"].user
        count_open_advertisement = (
            Advertisement.objects.filter(creator=user, status="OPEN").count()
        )
        if count_open_advertisement >= 10 and data.get('status') != 'CLOSED':
            raise ValidationError(
                f"Превышен лимит открытых объявлений, вы создали {count_open_advertisement} объявлений, "
                f"закройте объявление и повторите попытку."
            )
        return data


class FavoriteSerializer(serializers.ModelSerializer):
    advertisement = AdvertisementSerializer(read_only=True)

    class Meta:
        model = Favorite
        fields = "__all__"
