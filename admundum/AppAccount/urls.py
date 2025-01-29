from django.urls import path
from .views import (
    register_user,
    update_user,
    ProfileView,
    PassChangeView,
    password_changed,
    logout_user,
    error,
    modulo_admin,

)
urlpatterns = [
    path('registration/', register_user, name='register_user'),
    path('update_user/', update_user, name='update_user'),
    path('perfil/', ProfileView.as_view(), name='profile_user'),
    path('logout/', logout_user, name='logout'),
    path('password_changed/', password_changed, name='password_changed'),
    path('update_password/', PassChangeView.as_view(template_name='registration/update_password.html'), name='update_password'),
    path('error/', error, name='error'),
    path('admin/', modulo_admin, name='modulo_admin'),
]
