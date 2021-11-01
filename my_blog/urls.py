from django import urls
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.list_view, name='blog-home'),
    path('', views.PostListView.as_view(), name='blog-home'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.detail_view, name='blog-detail_view'),
    path('search/', views.search_view, name='blog-search_view'),
]