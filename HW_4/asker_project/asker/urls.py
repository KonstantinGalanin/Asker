from django.urls import path, include
from asker import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ask/', views.ask, name="ask"),
    path('hot/', views.hot, name="hot"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('question/<int:question_id>', views.question, name="question"),
    path('register/', views.register, name="register"),
    path('settings/', views.settings, name="settings"),
    path('tag/<str:tag_name>', views.tag, name="tag"),
]