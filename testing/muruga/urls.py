
from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(),name='muruga-home'),
    path('data/<int:pk>/', PostDetailView.as_view(),name='data_detail'),
    path('data/new/', PostCreateView.as_view(),name='data_create'),
    path('data/<int:pk>/update/', PostUpdateView.as_view(),name='data_update'),
    path('data/<int:pk>/delete/', PostDeleteView.as_view(),name='data_delete'),
    path('about/',views.about, name='muruga-about'),
]

