from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from access.models import AccessRoleRule
from access.serializers import (
    AccessRoleRuleSerializer,
    AccessRoleRuleUpdateSerializer,
)
from access.services import is_admin


class AccessRoleRuleListView(APIView):


    def get(self, request):
        if not request.user:
            return Response(
                {"detail": "Authentication required"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        if not is_admin(request.user):
            return Response(
                {"detail": "Forbidden"},
                status=status.HTTP_403_FORBIDDEN,
            )

        rules = AccessRoleRule.objects.select_related(
            "role", "element"
        )
        serializer = AccessRoleRuleSerializer(rules, many=True)
        return Response(serializer.data)


class AccessRoleRuleUpdateView(APIView):

    def put(self, request, rule_id):
        if not request.user:
            return Response(
                {"detail": "Authentication required"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        if not is_admin(request.user):
            return Response(
                {"detail": "Forbidden"},
                status=status.HTTP_403_FORBIDDEN,
            )

        try:
            rule = AccessRoleRule.objects.get(id=rule_id)
        except AccessRoleRule.DoesNotExist:
            return Response(
                {"detail": "Rule not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = AccessRoleRuleUpdateSerializer(
            rule, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            AccessRoleRuleSerializer(rule).data,
            status=status.HTTP_200_OK,
        )
