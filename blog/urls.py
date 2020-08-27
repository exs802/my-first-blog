from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('post/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('mycv/', views.show_cv, name='show_cv'),
    path('editcv/<int:pk>/', views.edit_cv, name='edit_cv'),
]