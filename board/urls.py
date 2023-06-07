from django.urls import path

from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name="post_list"),
    path('create/', views.PostCreate.as_view(), name="create_post"),
    path('<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
    path('<int:pk>/update/', views.PostUpdate.as_view(), name="update_post"),
    path('responses/', views.ResponseList.as_view(), name="response_list"),
    path('<int:pk>/respond/', views.ResponseCreate.as_view(), name="respond"),
    path('success/', views.SuccessView.as_view(), name="success"),
]