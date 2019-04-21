from django.urls import path
from django.contrib.auth.decorators import login_required
from profiles import views


urlpatterns = [
    path('profile/<username>/', login_required(views.ProfileView.as_view()), name='profile'),
    path('news/<username>/', login_required(views.NewsView.as_view()), name='news'),
    path('follow/', login_required(views.FollowView.as_view()), name='follow'),
    path('unfollow/', login_required(views.UnFollowView.as_view()), name='unfollow'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', login_required(views.MyLogoutView.as_view()), name='logout'),
]
