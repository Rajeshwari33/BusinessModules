from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.get_user_login, name="get_login"),
    path('user_credentials/', views.get_user_credentials, name="user_credentials"),
    path('user_list/', views.new_users_list, name="user_list"),
    path('create_user/', views.create_user_temp, name="create_user"),
    path('remove_user/', views.remove_user_temp, name="remove_user")
]