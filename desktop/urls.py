from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'desktop'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # URLs para gerenciamento de usuários
    path('usuarios/', views.user_list, name='user_list'),
    path('usuarios/novo/', views.user_create, name='user_create'),
    path('usuarios/<int:user_id>/', views.user_detail, name='user_detail'),
    path('usuarios/<int:user_id>/editar/', views.user_edit, name='user_edit'),
    path('usuarios/<int:user_id>/excluir/confirmar/', views.user_delete_confirm, name='user_delete_confirm'),
    path('usuarios/<int:user_id>/excluir/', views.user_delete, name='user_delete'),
    path('usuarios/<int:user_id>/redefinir-senha/', views.user_reset_password, name='user_reset_password'),
]