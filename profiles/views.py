from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from profiles.models import Contact
from posts.models import Post, PostRead


class ProfileView(View):
    def get(self, request, username):
        some_user = get_object_or_404(User, username=username)
        posts = Post.objects.filter(author=some_user)
        user = request.user

        contacts = Contact.objects.filter(user_from=user)
        contacts = [item.user_to for item in contacts]

        if some_user in contacts:
            followed = True
        else:
            followed = False

        context = {
            'some_user': some_user,
            'posts': posts,
            'followed': followed,
        }

        return render(request, 'profiles/profile.html', context)


class NewsView(View):
    def get(self, request, username):
        some_user = get_object_or_404(User, username=username)
        contacts = Contact.objects.filter(user_from=some_user)
        followed_users = [item.user_to for item in contacts]
        posts = Post.objects.filter(author__in=followed_users)

        user = request.user
        read_posts = PostRead.objects.filter(who_read=user)
        read_posts = [item.post for item in read_posts]

        context = {
            'some_user': some_user,
            'posts': posts,
            'read_posts': read_posts,
        } 
        
        return render(request, 'profiles/news.html', context)


class FollowView(View):
    def get(self, request):
        return redirect('/')
    def post(self, request):
        some_user_id = int(request.POST.get('follow'))
        some_user = get_object_or_404(User, id=some_user_id)

        contact = Contact.objects.get_or_create(user_from=request.user, user_to=some_user)
        
        return redirect('/profile/%s/' % some_user)


class UnFollowView(View):
    def get(self, request):
        return redirect('/')
    def post(self, request):
        some_user_id = int(request.POST.get('unfollow'))
        some_user = get_object_or_404(User, id=some_user_id)
        user = request.user

        contact = Contact.objects.get(user_from=request.user, user_to=some_user).delete()

        posts = Post.objects.filter(author=some_user)
        readpost = PostRead.objects.filter(who_read=user, post__in=posts).delete()
        
        return redirect('/profile/%s/' % some_user)
    

class MyLogoutView(LogoutView):
    template_name = 'profiles/logout.html'


class MyLoginView(LoginView):
    template_name = 'profiles/login.html'