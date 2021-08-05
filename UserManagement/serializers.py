from rest_framework import serializers
from UserManagement.models import Users, UserRoles


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class UsersRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoles
        fields = '__all__'
