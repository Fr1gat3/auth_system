from django.urls import path

from users.views import RegisterView, LoginView, UserMeView

app_name = 'users'

urlpatterns = [
    path('registration/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path("me/", UserMeView.as_view()),
]
