from rest_framework.serializers import ModelSerializer, ValidationError
from dj_rest_auth.serializers import UserDetailsSerializer
from users.models import UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class UserDetailsSerializer(UserDetailsSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        exclude = ("password", "username")

    def update(self, instance, validated_data):
        profile_data = validated_data.pop("profile", {})

        self.validate_allowed_fields(
            allowed_fields=[
                "first_name",
                "last_name",
                "second_name",
            ],
            validated_data=validated_data,
        )

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        self.update_profile(profile_data=profile_data, user_instance=instance)

        return instance

    def update_profile(self, profile_data, user_instance):
        if profile_data:
            self.validate_allowed_fields(
                allowed_fields=[
                    "location",
                ],
                validated_data=profile_data,
            )
            profile, _ = UserProfile.objects.get_or_create(user=user_instance)
            for attr, value in profile_data.items():
                setattr(profile, attr, value)
            profile.save()

    def validate_allowed_fields(self, allowed_fields, validated_data):
        errors = {
            field: f"{field} cannot be updated."
            for field in validated_data
            if field not in allowed_fields
        }

        if errors:
            raise ValidationError(errors)
