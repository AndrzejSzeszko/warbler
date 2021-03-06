"""warbler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from app_warbler import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ListAllTweetsView.as_view(), name='list-all-tweets'),
    path('create_tweet/', views.CreateTweetView.as_view(), name='create-tweet'),
    path('login/', auth_views.LoginView.as_view(template_name='app_warbler/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app_warbler/logout.html'), name='logout'),
    path('tweet_details/<int:pk>/', views.TweetDetailsView.as_view(), name='tweet-details'),
    path('update_tweet/<int:pk>/', views.UpdateTweetView.as_view(), name='update-tweet'),
    path('profile_details/<int:pk>/', views.ProfileDetailsView.as_view(), name='profile-details'),
    path('create_user/', views.CreateUserView.as_view(), name='create-user-sign-in'),
    path('create_message/<int:to_user>/', views.CreateMessageView.as_view(), name='create-message'),
    path('user_messages/<int:pk>/', views.ListUserMessagesView.as_view(), name='user-messages'),
    path('message_details/<int:pk>/', views.MessageDetailsView.as_view(), name='msg-details'),
    path('delete_user/<int:pk>/', views.DeleteUserView.as_view(), name='delete-user'),
    path('update_user/<int:pk>/', views.UpdateUserAndProfileView.as_view(), name='update-user'),
    path('delete_tweet/<int:pk>/', views.DeleteTweetView.as_view(), name='delete-tweet'),
    path('delete_comment/<int:pk>/', views.DeleteCommentView.as_view(), name='delete-comment'),
    path('password_reset', auth_views.PasswordResetView.as_view(template_name='app_warbler/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app_warbler/password_reset_done.html'), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app_warbler/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app_warbler/password_reset_complete.html'), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
