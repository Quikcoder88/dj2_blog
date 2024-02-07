from . import views
from django.urls import path

urlpatterns = [
    #path('', views.MyView.as_view()),
    path('add_ticket/', views.AddTicket.as_view()),
    path('list_ticket/', views.ListTicket.as_view(), name='list_ticket'),
    path('update_ticket/<int:pk>', views.UpdateTicket.as_view(), name='update_ticket'),
]