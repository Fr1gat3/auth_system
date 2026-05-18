from django.urls import path
from access.views import AccessRoleRuleListView, AccessRoleRuleUpdateView


urlpatterns = [
    path("access-rules/", AccessRoleRuleListView.as_view()),
    path("access-rules/<int:rule_id>/", AccessRoleRuleUpdateView.as_view()),
]
