from rest_framework import serializers
from access.models import AccessRoleRule


class AccessRoleRuleSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source="role.name", read_only=True)
    element = serializers.CharField(source="element.code", read_only=True)

    class Meta:
        model = AccessRoleRule
        fields = (
            "id",
            "role",
            "element",
            "read_permission",
            "read_all_permission",
            "create_permission",
            "update_permission",
            "update_all_permission",
            "delete_permission",
            "delete_all_permission",
        )


class AccessRoleRuleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessRoleRule
        fields = (
            "read_permission",
            "read_all_permission",
            "create_permission",
            "update_permission",
            "update_all_permission",
            "delete_permission",
            "delete_all_permission",
        )
