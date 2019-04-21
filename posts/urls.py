from django.urls import path
from django.contrib.auth.decorators import login_required
from posts import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('read/', login_required(views.ReadView.as_view()), name='read'),
    path('new_post/', login_required(views.NewPostView.as_view()), name='new_post'),
    path('add_post/', login_required(views.AddPostView.as_view()), name='add_post'),
    path('remove_post/', login_required(views.RemovePostView.as_view()), name='remove_post'),
]
