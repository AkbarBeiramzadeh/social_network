from django.shortcuts import render
from django.views import View


class PostsView(View):
    def get(self, request):
        return render(request, 'posts/posts.html')