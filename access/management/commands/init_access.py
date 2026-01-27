from django.core.management.base import BaseCommand
from access.models import Role, UserRole, BusinessElement, AccessRoleRule
from users.models import User


class Command(BaseCommand):
    help = "Initialize roles and access rules"

    def handle(self, *args, **kwargs):
        admin_role, _ = Role.objects.get_or_create(name="admin")

        elements = [
            ("orders", "Orders"),
            ("products", "Products"),
            ("users", "Users"),
            ("access_rules", "Access rules"),
        ]

        for code, name in elements:
            element, _ = BusinessElement.objects.get_or_create(
                code=code, name=name
            )

            AccessRoleRule.objects.get_or_create(
                role=admin_role,
                element=element,
                defaults={
                    "read_permission": True,
                    "read_all_permission": True,
                    "create_permission": True,
                    "update_permission": True,
                    "update_all_permission": True,
                    "delete_permission": True,
                    "delete_all_permission": True,
                },
            )

        first_user = User.objects.first()
        if first_user:
            UserRole.objects.get_or_create(
                user=first_user,
                role=admin_role
            )

        self.stdout.write(self.style.SUCCESS("Access system initialized"))
