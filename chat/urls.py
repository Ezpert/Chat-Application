from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('chat/', views.messagePage, name='chat-page'),
    path('signup/', views.signUp, name='sign-up'),
    # path('send_message/', views.send_message, name='send_message'),
]