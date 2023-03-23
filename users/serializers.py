from rest_framework.serializers import ModelSerializer, SlugRelatedField, SerializerMethodField

from users.models import User, Location


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ["password"]


class UserListSerializer(ModelSerializer):
    total_ads = SerializerMethodField()

    def get_total_ads(self, user):
        return user.ad_set.filter(is_published=True).count()

    class Meta:
        model = User
        fields = ["username", "total_ads"]


class UserDetailSerializer(ModelSerializer):
    location = SlugRelatedField(queryset=Location.objects.all(), slug_field='name')

    class Meta:
        model = User
        exclude = ["password"]


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"
