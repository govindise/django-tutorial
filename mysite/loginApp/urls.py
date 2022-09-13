from django.urls import path
from knox import views as knox_view
from .views import LoginView, RegisterView, getUser

app_name = 'loginApp'
urlpatterns = [
    path('', getUser, name="index"),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', knox_view.LogoutView.as_view(), name="logout"),
]