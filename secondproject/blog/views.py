from django.core import paginator
from django.db.models import query
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogForm
# Create your views here.

def home(request):
    blogs = Blog.objects.order_by('-pub_date')

    query = request.GET.get('query')
    if query:
        blogs = Blog.objects.filter(title__icontains=query).order_by('-pub_date')

    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    paginated_blogs = paginator.get_page(page)
    return render(request, 'home.html', {'blogs': paginated_blogs})

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html', {'blog': blog})

def new_with_django_form(request):
    form = BlogForm()
    return render(request, 'new_with_django_form.html', {'form': form})

# def new(request):
#     return render(request, 'new.html')

def create_with_django_form(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.pub_date = timezone.now()
        new_blog.save()
        return redirect('blog:detail', new_blog.id)
    return redirect('home')

# def create(request):
#     new_blog = Blog()
#     new_blog.title = request.POST['title']
#     new_blog.writer = request.POST['writer']
#     new_blog.body = request.POST['body']
#     new_blog.pub_date = timezone.now()
#     try:
#         new_blog.image = request.FILES['image']
#     except:
#         print()
#     # new_blog.image = request.FILES['image']
#     new_blog.save()
#     return redirect('blog:detail', new_blog.id)

def update(request, id):
    blog = Blog.objects.get(id = id)
    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.body = request.POST["body"]
        blog.save()
        return redirect('blog:detail', blog.id)
    return render(request, 'update.html', {'blog': blog})

def delete(request, id):
    blog = Blog.objects.get(id = id)
    blog.delete()
    return redirect("home")