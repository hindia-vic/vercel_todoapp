from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('todo',views.todo,name='todo'),
    path('content/<int:Todo_id>/',views.content, name='content'),
    path('delete/<int:Todo_id>/',views.delete,name='delete'),
    path('edit/<int:Todo_id>/',views.edit,name='edit'),
    path('update/<int:Todo_id>/',views.update,name='update'),
    path('register',views.register,name='register'),
    path('accounts/login/',views.login,name='login'),
    path('finish/<int:Todo_id>/',views.finish,name='finish'),
    path('logout',views.logout,name='logout'),
    path('reset_password/',auth_views.PasswordResetView.as_view(),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]