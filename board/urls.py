from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('notice/', views.notice_list, name='notice_list'),
    path('notice/<int:pk>/', views.notice_detail, name='notice_detail'),
    path('activity/', views.activity_list, name='activity_list'),
    path('gallery/', views.gallery_list, name='gallery_list'),
    path('members/', views.member_list, name='member_list'),
    path('activity/<int:pk>/', views.activity_detail, name='activity_detail'),
]