from django.urls import path
from .views import (
    AboutPostView,
    TeamPostView,
    NewsPostView,
    BlogPostView,
    ContactPostView,
    PoleListView,
    PoleUpdateView,
    PoleDeleteView,
    PoleCreateView,
    # PoleCreateImageView,
    PoleDetailView,
    index_detail,
    to_rezerv,
    ProfileView
)
urlpatterns = [
    path('about/', AboutPostView.as_view(), name='about'),
    path('team/', TeamPostView.as_view(), name='team'),
    path('news/', NewsPostView.as_view(), name="news"),
    path('blog/', BlogPostView.as_view(), name='blog'),
    path('contact/', ContactPostView.as_view(), name='contact'),
    path('<int:pk>/edit/', PoleUpdateView.as_view(), name='pole_edit'),
    path('<int:pk>/', PoleDetailView.as_view(), name='pole_detail'),
    path('<int:pk>/delete/', PoleDeleteView.as_view(), name='pole_delete'),
    path('new/', PoleCreateView.as_view(), name='pole_new'),
    path('', PoleListView.as_view(), name='pole_list'),
    # path('<int:pk>/create_image/', PoleCreateImageView.as_view(), name='pole_create_image'),
    path('detail/<int:pk>/', index_detail, name='detail'),
    path('rezerv/', to_rezerv, name='rezerv'),
    path('profile/', ProfileView.as_view(), name='profile')
]



