from rest_framework import serializers

from app_media.models import Media


class MediaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = "__all__"
        extra_kwargs = {
            'is_active': {'default': True}
        }