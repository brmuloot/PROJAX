from django.urls import path

from . import views


app_name = "blog"
urlpatterns = [
    path('', views.index, name='index'),
    path("<int:post_id>/detail/", views.detail, name="detail") ,
    path('<int:post_id>/add-comment/', views.comment, name='add-comment'),
    path('submit_comment/<int:post_id>/', views.submit_comment, name='submit_comment'),
]