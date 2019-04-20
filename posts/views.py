from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
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