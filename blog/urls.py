from django.urls import path
from .views import BlogViews, BlogCreateView, BlogDetail, BlogUpdated, BlogDelete

app_name='blog'

urlpatterns = [
    path('', BlogViews.as_view(), name='home'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('<int:pk>/detail/', BlogDetail.as_view(), name='detail'),
    path('<int:pk>/updated/', BlogUpdated.as_view(), name='updated'),
    path('<int:pk>/delete/', BlogDelete.as_view(), name='delete'),
]
