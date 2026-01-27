from access.models import UserRole, AccessRoleRule


def has_permission(user, element_code, action):
    roles = UserRole.objects.filter(user=user).values_list("role_id", flat=True)

    if not roles:
        return False

    rules = AccessRoleRule.objects.filter(
        role_id__in=roles,
        element__code=element_code,
    )

    for rule in rules:
        if action == "read" and rule.read_permission:
            return True
        if action == "create" and rule.create_permission:
            return True
        if action == "update" and rule.update_permission:
            return True
        if action == "delete" and rule.delete_permission:
            return True

    return False
