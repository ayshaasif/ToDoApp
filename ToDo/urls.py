from django.urls import path

from . import views


urlpatterns = [
    path('',views.home,name="myhome"),
    path('display',views.showReminders,name = "showReminder"),
    path('create', views.createReminders, name="createReminder"),
    path('filter/<int:post_id>/',views.filterReminder,name="filterReminder"),
    path('delete', views.deleteReminder, name="deleteReminder"),
    path('update/<str:pk>/', views.updateReminder, name="updateReminder"),
]