from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.http import JsonResponse
from posts.models import Post, PostRead


class IndexView(View):
    def get(self, request):
        posts = Post.objects.all()

        context = {
            'posts': posts,
        } 
        
        return render(request, 'posts/index.html', context)


class ReadView(View):
    def get(self, request):
        return redirect('/')
    def post(self, request):
        read = request.POST.get('read')
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=int(post_id))
        user = request.user
        
        if read == '0':
            readpost = PostRead.objects.get_or_create(who_read=user, post=post)
        if read == '1':
            readpost = PostRead.objects.get(who_read=user, post=post).delete()

        return redirect('/news/%s/' % user)


class NewPostView(View):
    def get(self, request):
        return render(request, 'posts/add_post.html', {})


class AddPostView(View):
    def get(self, request):
        return redirect('/')
    def post(self, request):
        title = request.POST.get('title')
        text = request.POST.get('text')
        user = request.user
        
        post = Post.objects.create(author=user, text=text, title=title)

        return redirect('/profile/%s/' % user)


class RemovePostView(View):
    def get(self, request):
        return redirect('/')
    def post(self, request):
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=int(post_id)).delete()
        user = request.user

        return JsonResponse({})