from django.urls import path

from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name="post_list"),
    path('create/', views.PostCreate.as_view(), name="create_post"),
    path('<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
    path('<int:pk>/update/', views.PostUpdate.as_view(), name="post_update"),
    path('responses/', views.ResponseList.as_view(), name="response_list"),
    path('<int:pk>/responses/', views.PostResponseList.as_view(), name="response_post"),
    path('<int:pk>/respond/', views.ResponseCreate.as_view(), name="respond"),
    path('responses/<int:pk>/accept/', views.response_accept, name="accept"),
    path('responses/<int:pk>/deny/', views.response_not_accept, name="deny"),
    path('success/', views.SuccessView.as_view(), name="success"),
]