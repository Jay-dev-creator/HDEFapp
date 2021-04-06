from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import  static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path('tutoring', views.tutoring, name='tutoring'),
    path('upload/', views.upload, name='upload'),
    path('upload_list/', views.upload_list, name='upload_list'),
    path('upload_item/', views.upload_item, name='upload_item'),
    path('donations/', views.index, name='index'),
    path('accounts/sign_up/', views.sign_up, name='sign_up'),
    path('logout/', views.logout_request, name='logout'),
    path('about/', views.about, name='about'),
    path('gratitude', views.gratitude, name='gratitude'),


    #reset password
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="accounts/reset_password.html"),
         name='reset_password'),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
         name='password_reset_done'),
    path('reset/<uib64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
         name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)