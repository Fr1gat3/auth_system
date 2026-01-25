from django.urls import path

from users.views import RegisterView, LoginView

app_name = 'users'

urlpatterns = [
    path('registration/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
]
