from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Post,Category, About
import os
from django.conf import settings
from django.core.files.storage import default_storage

def home(request):
    latest_posts = Post.objects.all().order_by('-date_posted')[:3] 
    return render(request, 'index.html', {'latest_posts': latest_posts})

def upload_file(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        uploaded_file = request.FILES['upload']
        uploaded_file_url = handle_uploaded_file(uploaded_file)
        return JsonResponse({'url': uploaded_file_url})
    return JsonResponse({'error': 'POST method with file upload required'})

def handle_uploaded_file(uploaded_file):
    path = default_storage.save('uploads/' + uploaded_file.name, uploaded_file)
    return os.path.join(settings.MEDIA_URL, path)

def post_detail(request, post_id):
    post = get_object_or_404(Post, url=post_id)
    return render(request, 'post_detail.html', {'post': post})

def articles(request):
    categories = Category.objects.all().order_by('order')
    posts = Post.objects.all().order_by('-date_posted') 
    category_name = request.GET.get('category')
    
    if category_name:
        posts = Post.objects.filter(category__name=category_name).order_by('-date_posted')
    else:
        posts = Post.objects.all().order_by('-date_posted')

    return render(request, 'articles/articles.html', {'categories': categories, 'posts': posts})


def about(request):
    about_update = get_object_or_404(About) 
    return render(request, 'about/about.html', {'about_update': about_update})

def privacy(request):
    return render(request, 'privacy/privacy.html')


